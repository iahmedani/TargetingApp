import pandas as pd
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.files.base import ContentFile
from dtale.views import startup
import io
import dtale.global_state as global_state
from django.conf import settings
from django.contrib import messages
import os
from datetime import datetime
from openpyxl import load_workbook
from .forms import ExcelCompareForm
from openpyxl.styles import PatternFill
from io import BytesIO
from openpyxl.utils.dataframe import dataframe_to_rows



from .data_quality_utils import (
    read_dataset,
    find_duplicate_id_number,
    find_duplicate_mobile_number,
    find_q5_a5_error,
    find_q6_a6_error,
    find_child_under_5_error,
    find_potential_hoh_duplicates,
    add_error_remarks,
    merge_error_subsets,
    produce_final_excel
)
from io import BytesIO
import xlsxwriter  # Ensure xlsxwriter is installed

global_state.set_app_settings(dict(enable_custom_filters=True, optimize_dataframe=True, ignore_duplicate=True,  lock_header_menu=True, main_title = 'Tageting DQA App'))


def index(request):
    return HttpResponse("""
        <h1>Django App with D-Tale</h1>
        <p><a href="/data_quality/create-df">Generate sample dataframe in D-Tale</a></p>
        <p><a href="/data_quality/import-data">Import CSV file to D-Tale</a></p>
    """)
    
def create_df(request):
    df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]))
    instance = startup(data=df, ignore_duplicate=True)
    return redirect(f"/flask/dtale/main/{instance._data_id}")

# create data upload csv file and display in D-Tale

class ImportDataView(View):
    def get(self, request):
        return render(request, 'upload.html')
    
    def post(self, request):
        if 'file' not in request.FILES:
            return HttpResponse("No file uploaded", status=400)
        
        file = request.FILES['file']
        
        # Save the file temporarily
        path = default_storage.save('tmp/'+file.name, ContentFile(file.read()))
        
        try:
            # Read the CSV file
            with default_storage.open(path) as f:
                df = pd.read_csv(io.StringIO(f.read().decode('utf-8')))
            
            # Start D-Tale with the imported data
            instance = startup(data=df)
            # print(instance.)
            url = f"/flask/dtale/main/{instance._data_id}"
            print(url)
            # Redirect to D-Tale
            return render(request, 'dtale.html', context={'url': url})
        except Exception as e:
            return HttpResponse(f"Error processing file: {str(e)}", status=400)
        finally:
            # Clean up the temporary file
            default_storage.delete(path)
            
def dqa_analysis(request):
    return render(request, 'dtale.html', context={'url': request.GET.get('url')})

def excel_upload_view(request):
    if request.method == 'POST':
        if 'excel_file' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('upload_excel')
        
        excel_dqa_file = request.FILES['excel_file']
        
        # Check if the uploaded file is an Excel (.xlsx) file
        if not excel_dqa_file.name.endswith('.xlsx'):
            messages.error(request, 'Please upload a valid .xlsx file')
            return redirect('upload_excel')

        # Generate a unique filename by appending the current timestamp
        original_filename = excel_dqa_file.name
        file_extension = os.path.splitext(original_filename)[1]  # Get the file extension
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Get the current timestamp
        unique_filename = f"{os.path.splitext(original_filename)[0]}_{timestamp}{file_extension}"

        # Define the folder to save the file in
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'excel_files'))
        
        # Save the file with the unique filename
        filename = fs.save(unique_filename, excel_dqa_file)
        file_url = fs.url(filename)

        # Display success message
        messages.success(request, f'File uploaded successfully: {file_url}')
        
        context = {'file_url': file_url}
        return render(request, 'upload_excel.html', context=context)
        
        
    # Render the file upload form if the request method is GET
    return render(request, 'upload_excel.html')

def std_data_analysis1(request):
    file_url = request.GET.get('file_url')
    
    if file_url:
        # Extract the filename from the file URL
        file_name = os.path.basename(file_url)
        
        # Construct the full file path based on MEDIA_ROOT
        file_path = os.path.join(settings.MEDIA_ROOT, 'excel_files', file_name)
        print(file_path)
        
        if not os.path.exists(file_path):
            return HttpResponse("File not found", status=404)

        try:
            # Use a generator to stream the data in chunks manually
            def excel_data_generator(file_path):
                wb = load_workbook(file_path, read_only=True)
                ws = wb.active
                
                # Read rows in chunks manually (adjust as needed)
                chunk_size = 1000
                rows = ws.iter_rows(values_only=True)
                chunk = []
                for idx, row in enumerate(rows):
                    chunk.append(row)
                    if (idx + 1) % chunk_size == 0:
                        yield pd.DataFrame(chunk).to_json(orient='records')
                        chunk = []
                
                # Yield the remaining rows if any
                if chunk:
                    yield pd.DataFrame(chunk).to_json(orient='records')

            # Create a StreamingHttpResponse for large data
            response = StreamingHttpResponse(excel_data_generator(file_path), content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'

            return response

        except Exception as e:
            return HttpResponse(f"Error processing the file: {str(e)}", status=500)
    else:
        return HttpResponse("No file URL provided", status=400)


def calculate_time_difference(df, start_col='start', end_col='end'):
    """
    Calculate the difference in minutes between start_time and end_time and return a new DataFrame with the result.

    :param df: pandas DataFrame containing the start and end time columns
    :param start_col: Name of the start time column (default is 'start_time')
    :param end_col: Name of the end time column (default is 'end_time')
    :return: A new DataFrame with the original data and an additional column 'time_difference_minutes'
    """

    # Create a copy of the DataFrame to avoid modifying the original
    df_copy = df.copy()

    # Ensure that start_time and end_time are in datetime format
    df_copy[start_col] = pd.to_datetime(df_copy[start_col], errors='coerce')
    df_copy[end_col] = pd.to_datetime(df_copy[end_col], errors='coerce')

    # Calculate the time difference in minutes
    df_copy['time_difference_minutes'] = (df_copy[end_col] - df_copy[start_col]).dt.total_seconds() / 60

    # Handling potential missing or invalid values by replacing them with NaN or a default value (e.g., 0)
    df_copy['time_difference_minutes'] = df_copy['time_difference_minutes'].fillna(0)

    return df_copy


def std_data_analysis(request):
    file_url = request.GET.get('file_url')
    
    if file_url:
        # Extract the filename from the file URL
        file_name = os.path.basename(file_url)
        
        # Construct the full file path based on MEDIA_ROOT
        file_path = os.path.join(settings.MEDIA_ROOT, 'excel_files', file_name)
        
        df = read_dataset(file_path)

        # Section Two: Duplicate id_number
        dup_id_num = find_duplicate_id_number(df)
        dup_id_num = add_error_remarks(
            dup_id_num,
            'Duplicate ID Number:',
            'Duplicate ID number identified based on paper or electronic tazkira (column name id_number). Please review the entries and determine if the data is valid, or if the duplicate records should be removed.'
        )

        # Section Three: Duplicate Mobile Number
        dup_mob_rows = find_duplicate_mobile_number(df)
        dup_mob_rows = add_error_remarks(
            dup_mob_rows,
            'Duplicate Mobile Number',
            'Duplicate mobile number detected (column name mob). Please review and determine whether the mobile numbers need correction or if any duplicates should be removed.'
        )

        # Section Four: Q5/A5 error
        a5_error = find_q5_a5_error(df)
        a5_error = add_error_remarks(
            a5_error,
            'Vulnerability Q5 Error: (The head of the household has a disability.)',
            'Inconsistency found in Vulnerability Question 5 (column A5). The household is marked as disabled (column HH_head has value 3), but Question 5 indicates "No". Please review the data and correct this discrepancy.'
        )

        # Section Five: Q6/A6 Error
        a6_error = find_q6_a6_error(df)
        a6_error = add_error_remarks(
            a6_error,
            'Vulnerability Q6 Error: (The household has more than 3 children under the age of 5.)',
            'Vulnerability Question 6 has a potential issue: either Q6 (column name A6 is marked 1) is marked "Yes" but there are fewer (in column child_5Num) than 4 children under 5, or Q6 is marked "No" but there are more than 3 children under 5. Please verify the data and make necessary corrections.'
        )

        # Section Six: Children Under 5 Error
        child_5_error = find_child_under_5_error(df)
        child_5_error = add_error_remarks(
            child_5_error,
            'Child Under 5 Error (Do you have  children under 5 in this HH? )',
            'Discrepancy found: The household is marked as having a child under 5 (column name child_5 has value 1), but the number of children under 5 is recorded as 0. Please verify and correct this error in the data.'
        )

        # Section Seven: Potential Head of Household Duplication
        duplicate_rows = find_potential_hoh_duplicates(df)
        if not duplicate_rows.empty:
            duplicate_rows = add_error_remarks(
                duplicate_rows,
                'Potential Head of Household Duplicate',
                'Possible duplicate head of household found based on Beneficiary Name, Father Name, and ID Number. Please review the data to confirm whether it is a valid entry or if duplicates need to be corrected or removed.'
            )

        # Section Eight: Merge Errors
        subsets = [dup_id_num, dup_mob_rows, a5_error, a6_error, child_5_error]
        if not duplicate_rows.empty:
            subsets.append(duplicate_rows)
        merged_errors = merge_error_subsets(subsets)

        # Section Nine: Produce final excel workbook
        df_with_errors, df_without_errors = produce_final_excel(df, merged_errors)
        df_without_errors.drop(columns=['name_ben_clean',	'ben_fath_clean',	'id_number_clean'], inplace=True)
        df_with_errors.drop(columns=['name_ben_clean',	'ben_fath_clean',	'id_number_clean'], inplace=True)
        
        avg_time = calculate_time_difference(df)
        
        avg_time = avg_time.pivot_table(values='time_difference_minutes', index=['cp','username'], columns='vul', aggfunc=['mean','count'], margins=True, margins_name='Total')
        
        df_summary = pd.pivot_table(
                                df, 
                                values='KEY', 
                                index=['cp','assessmentType'],
                                columns='vul', 
                                aggfunc='count', 
                                margins=True,       # Adds the total row
                                margins_name='Total'  # Renames the total row to 'Total'
                            ).reset_index()
        
        df_summary1 = pd.pivot_table(
                                df, 
                                values='KEY', 
                                index=['cp','assessmentType','SB-cfac_name','username','vul'],
                                columns='today', 
                                aggfunc='count', 
                                margins=True,       # Adds the total row
                                margins_name='Total'  # Renames the total row to 'Total'
                            ).reset_index()
        
        # df_with_errors = df_with_errors[df_with_errors['vul']=='Yes']
        # df_without_errors = df_without_errors[df_without_errors['vul']=='Yes']
        df_with_errors_summary = pd.pivot_table(
                                        df_with_errors, 
                                        values='KEY', 
                                        index='error_type', 
                                        aggfunc='count', 
                                        margins=True,       # Adds the total row
                                        margins_name='Total'  # Renames the total row to 'Total'
                                    ).reset_index()
        df_with_errors_summary = df_with_errors_summary.rename(columns={'error_type': 'Error Type', 'KEY':'Count'})

        


        # Create an in-memory output file for the new workbook
        output = BytesIO()

        # Use a context manager to handle the Excel writer
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet
            df_summary.to_excel(writer, sheet_name='Summary', index=False)
            df_summary1.to_excel(writer, sheet_name='DetailSummary', index=False)
            avg_time.to_excel(writer, sheet_name='Avg_Time', index=True)
            df_with_errors_summary.to_excel(writer, sheet_name='Error_Summary', index=False)
            df_with_errors.to_excel(writer, sheet_name='Errors', index=False)
            df_without_errors.to_excel(writer, sheet_name='No_Errors', index=False)
            # No need to call writer.close(); it's handled by the context manager

        # Rewind the buffer
        output.seek(0)

        # Set up the HttpResponse
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        processed_file_name = f'{file_name.strip(".xlsx")}_processed.xlsx'
        response['Content-Disposition'] = f'attachment; filename="{processed_file_name}"'

        return response
    else:
        return HttpResponse("No file URL provided", status=400)


def cfac_excel_upload_view(request):
    if request.method == 'POST':
        if 'excel_file' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('upload_excel')
        
        excel_dqa_file = request.FILES['excel_file']
        
        # Check if the uploaded file is an Excel (.xlsx) file
        if not excel_dqa_file.name.endswith('.xlsx'):
            messages.error(request, 'Please upload a valid .xlsx file')
            return redirect('upload_excel')

        # Generate a unique filename by appending the current timestamp
        original_filename = excel_dqa_file.name
        file_extension = os.path.splitext(original_filename)[1]  # Get the file extension
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Get the current timestamp
        unique_filename = f"{os.path.splitext(original_filename)[0]}_{timestamp}{file_extension}"

        # Define the folder to save the file in
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'excel_files'))
        
        # Save the file with the unique filename
        filename = fs.save(unique_filename, excel_dqa_file)
        file_url = fs.url(filename)

        # Display success message
        messages.success(request, f'File uploaded successfully: {file_url}')
        
        context = {'file_url': file_url}
        return render(request, 'upload_excel_cfac.html', context=context)
        
        
    # Render the file upload form if the request method is GET
    return render(request, 'upload_excel_cfac.html')



from .cfac_village_list_utils import (
    load_excel_file,
    clean_dataframe,
    check_required_columns,
    ensure_remarks_column,
    map_province_and_district_codes,
    add_remarks_for_missing_codes,
    check_missing_focal_point_contacts,
    create_cfac_codes,
    create_cfac_list,
    create_village_codes,
    create_village_list,
    save_to_excel,
)

def process_excel_file(request):
    file_url = request.GET.get('file_url')
    if file_url:
        # Extract the filename from the file URL
        file_name = os.path.basename(file_url)

        # Construct the full file path based on MEDIA_ROOT
        file_path = os.path.join(settings.MEDIA_ROOT, 'excel_files', file_name)

        # Step 1: Load the Excel file
        df = load_excel_file(file_path)

        # Step 2: Clean the DataFrame
        df = clean_dataframe(df)

        # Step 3: Check for required columns
        required_columns = ['AO', 'Area', 'Province', 'District', 'Village', 'Nahia', 'CFAC Name',
                            'CFAC FP 1', 'FP1 Number', 'CFAC FP2', 'FP2 Number', 'Remarks']
        columns_present, missing_columns = check_required_columns(df, required_columns)
        if not columns_present:
            return HttpResponse(f"Missing required columns: {', '.join(missing_columns)}", status=400)

        # Ensure 'Remarks' column exists
        df = ensure_remarks_column(df)

        # Step 4: Map province and district codes
        province_file = os.path.join(settings.MEDIA_ROOT, 'data_files', 'province.csv')
        district_file = os.path.join(settings.MEDIA_ROOT, 'data_files', 'district.csv')
        df = map_province_and_district_codes(df, province_file, district_file)

        # Step 5: Add remarks for missing codes
        df = add_remarks_for_missing_codes(df)

        # Step 6: Check for missing focal point contacts
        df = check_missing_focal_point_contacts(df)

        # Step 7: Separate valid and error rows
        df['Remarks'] = df['Remarks'].fillna('').astype(str)
        df_valid = df[df['Remarks'] == '']
        df_errors = df[df['Remarks'] != '']

        # Step 8: Separate data by area type
        urban_df = df_valid[df_valid['Area'] == 'Urban Area'].copy()
        rural_df = df_valid[df_valid['Area'] == 'Rural Area'].copy()

        # Step 9: Create CFAC codes
        urban_df = create_cfac_codes(urban_df, is_urban=True)
        rural_df = create_cfac_codes(rural_df, is_urban=False)

        # Step 10: Create CFAC list
        cfac_df = pd.concat([urban_df, rural_df], ignore_index=True)
        cfac_list = create_cfac_list(cfac_df)

        # Step 11: Create village codes
        urban_df = create_village_codes(urban_df, is_urban=True)
        rural_df = create_village_codes(rural_df, is_urban=False)

        # Step 12: Create village list
        village_df = pd.concat([urban_df, rural_df], ignore_index=True)
        village_list = create_village_list(village_df)

        # Step 13: Prepare data for Excel output
        output = BytesIO()
        output_file_name = f"{os.path.splitext(file_name)[0]}_output.xlsx"
        df_dict = {
            'cfac_list': cfac_list,
            'village_list': village_list,
            'original_data': df,
            'errors': df_errors,
        }

        # Save to Excel
        save_to_excel(df_dict, output)

        # Set up the HttpResponse
        response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{output_file_name}"'

        return response
    else:
        return HttpResponse("No file URL provided", status=400)


def deduplicate_upload(request):
    if request.method == 'POST':
        if 'excel_file' not in request.FILES:
            messages.error(request, 'No file selected')
            return redirect('upload_excel')
        
        excel_dqa_file = request.FILES['excel_file']
        
        # Check if the uploaded file is an Excel (.xlsx) file
        if not excel_dqa_file.name.endswith('.xlsx'):
            messages.error(request, 'Please upload a valid .xlsx file')
            return redirect('upload_excel')

        # Generate a unique filename by appending the current timestamp
        original_filename = excel_dqa_file.name
        file_extension = os.path.splitext(original_filename)[1]  # Get the file extension
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Get the current timestamp
        unique_filename = f"{os.path.splitext(original_filename)[0]}_{timestamp}{file_extension}"

        # Define the folder to save the file in
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'excel_files'))
        
        # Save the file with the unique filename
        filename = fs.save(unique_filename, excel_dqa_file)
        file_url = fs.url(filename)

        # Display success message
        messages.success(request, f'File uploaded successfully: {file_url}')
        
        context = {'file_url': file_url}
        return render(request, 'deduplicate.html', context=context)
        
        
    # Render the file upload form if the request method is GET
    return render(request, 'deduplicate.html')


def deduplicate_export(request):
    file_url = request.GET.get('file_url')
    if file_url:
        # Extract the filename from the file URL
        file_name = os.path.basename(file_url)

        # Construct the full file path based on MEDIA_ROOT
        file_path = os.path.join(settings.MEDIA_ROOT, 'excel_files', file_name)

        # Step 1: Load the Excel file
        df = load_excel_file(file_path)
        
        df_deduplicated = df.drop_duplicates()

       
        # Step 13: Prepare data for Excel output
        output = BytesIO()
        output_file_name = f"{os.path.splitext(file_name)[0]}_output.xlsx"
        df_dict = {
            'deduplicate_data': df_deduplicated,
            'original_data': df
        }

        # Save to Excel
        save_to_excel(df_dict, output)

        # Set up the HttpResponse
        response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{output_file_name}"'

        return response
    else:
        return HttpResponse("No file URL provided", status=400)


def compare_excel_documents(request):
    if request.method == 'POST':
        form = ExcelCompareForm(request.POST, request.FILES)
        if form.is_valid():
            first_file = request.FILES['first_document']
            second_file = request.FILES['second_document']

            try:
                # Read all sheets from both Excel files into dictionaries of DataFrames
                first_df_dict = pd.read_excel(first_file, sheet_name=None)
            except Exception as e:
                messages.warning(request, f'Error reading the first Excel file: {e}')
                return render(request, 'upload_c.html', {
                    'form': form
                })

            try:
                second_df_dict = pd.read_excel(second_file, sheet_name=None)
            except Exception as e:
                messages.warning(request, f'Error reading the second Excel file: {e}')
                return render(request, 'upload_c.html', {
                    'form': form
                })

            # Reset the file pointer of the second file for OpenPyXL
            second_file.seek(0)
            try:
                wb = load_workbook(second_file)
            except Exception as e:
                messages.warning(request, f'Error loading the second Excel file with OpenPyXL: {e}')
                return render(request, 'upload_c.html', {
                    'form': form,
                })

            # Define the fill for highlighting differences (yellow color)
            highlight_fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')

            report = []

            # Iterate through each sheet present in both documents
            for sheet_name in first_df_dict.keys():
                if sheet_name in second_df_dict:
                    first_sheet_df = first_df_dict[sheet_name]
                    second_sheet_df = second_df_dict[sheet_name]

                    # Ensure both sheets have the same shape
                    if first_sheet_df.shape != second_sheet_df.shape:
                        report.append({
                            'Sheet': sheet_name,
                            'Issue': f'Sheet shapes differ between documents. ({first_sheet_df.shape} vs. {second_sheet_df.shape})'
                        })
                        continue  # Skip comparison for this sheet

                    # Access the corresponding worksheet in OpenPyXL
                    ws = wb[sheet_name]

                    # Iterate through each cell to find differences
                    for row_idx in range(1, second_sheet_df.shape[0] + 1):
                        for col_idx in range(1, second_sheet_df.shape[1] + 1):
                            first_value = first_sheet_df.iat[row_idx - 1, col_idx - 1]
                            second_value = second_sheet_df.iat[row_idx - 1, col_idx - 1]

                            # Handle NaN values
                            if pd.isna(first_value) and pd.isna(second_value):
                                continue  # Both are NaN, consider equal
                            if first_value != second_value:
                                # Highlight the cell in the second workbook
                                cell = ws.cell(row=row_idx, column=col_idx)
                                cell.fill = highlight_fill

                                # Record the difference in the report
                                report.append({
                                    'Sheet': sheet_name,
                                    'Cell': cell.coordinate,
                                    'First Document Value': first_value,
                                    'Second Document Value': second_value
                                })
                else:
                    # Sheet is missing in the second document
                    report.append({
                        'Sheet': sheet_name,
                        'Issue': 'Sheet missing in the second document.'
                    })

            # If there are differences, add the Comparison Report sheet
            if report:
                # Create a DataFrame from the report
                report_df = pd.DataFrame(report)

                # Add a new sheet for the report
                report_sheet_title = 'Comparison Report'
                if report_sheet_title in wb.sheetnames:
                    # If the report sheet already exists, remove it to avoid duplication
                    std = wb[report_sheet_title]
                    wb.remove(std)

                report_ws = wb.create_sheet(title=report_sheet_title)

                # Write the DataFrame to the report sheet
                for r_idx, row in enumerate(dataframe_to_rows(report_df, index=False, header=True), 1):
                    for c_idx, value in enumerate(row, 1):
                        cell = report_ws.cell(row=r_idx, column=c_idx, value=value)
                        # Optionally, style the header row
                        if r_idx == 1:
                            cell.font = cell.font.copy(bold=True)

                # Save the modified workbook to a BytesIO buffer
                buffer = BytesIO()
                try:
                    wb.save(buffer)
                except Exception as e:
                    messages.error(request, f'Error saving the modified Excel file: {e}')
                    return render(request, 'upload_c.html', {
                        'form': form
                    })

                buffer.seek(0)  # Reset buffer position

                # Prepare the HTTP response with the modified Excel file
                response = HttpResponse(
                    buffer,
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=Compared_Document.xlsx'
                return response
            else:
                # No differences found
                messages.success(request, 'No differences found between the two documents.')
                return render(request, 'upload_c.html', {
                    'form': form
                })

    else:
        form = ExcelCompareForm()

    return render(request, 'upload_c.html', {'form': form})



    
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import io
import os
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

def prepare_final_list(request):
    if request.method == 'POST':
        # Get the uploaded file and passwords
        excel_file = request.FILES['excel_file']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']

        # Load the workbook with openpyxl
        wb = load_workbook(filename=excel_file, read_only=False, data_only=True)
        ws = wb.active

        # Extract the merged cell value from the first row
        merged_value = None
        for merged_range in ws.merged_cells.ranges:
            if merged_range.min_row == 1:
                # Get the cell value
                cell = ws.cell(row=merged_range.min_row, column=merged_range.min_col)
                merged_value = cell.value
                break

        # Remove the first row
        ws.delete_rows(1)

        # Save the modified workbook to a BytesIO object
        temp_excel = io.BytesIO()
        wb.save(temp_excel)
        temp_excel.seek(0)

        # Read the modified Excel file into pandas DataFrame
        df = pd.read_excel(temp_excel)

        # Optionally, add the merged cell data back into the DataFrame
        if merged_value is not None:
            df['MergedData'] = merged_value

        # Create a summary of the 'status' column
        status_counts = df['status'].value_counts().reset_index()
        status_counts.columns = ['status', 'count']

        # Create DataFrames for 'Selected HH' and 'Rejected HH'
        selected_hh = df[df['status'].str.contains('Selected:')]
        selected_regular = selected_hh[selected_hh['assessmentType'].str.contains('Regular')]
        selected_replacement = selected_hh[selected_hh['assessmentType'].str.contains('Replacement')]
        selected_appeal = selected_hh[selected_hh['assessmentType'].str.contains('Appeal')]
        rejected_hh = df[df['status'].str.contains('Rejected:')]

        # Prepare the Excel writer using xlsxwriter with password1 to open the file
        output = io.BytesIO()
        writer = pd.ExcelWriter(
            output,
            engine='xlsxwriter',
            # engine_kwargs={'options': {'password': password1}}
        )

        # Write DataFrames to different sheets
        # df.to_excel(writer, index=False, sheet_name='Sheet1')
        status_counts.to_excel(writer, index=False, sheet_name='Summary')
        selected_hh.to_excel(writer, index=False, sheet_name='All Selected HH')
        selected_regular.to_excel(writer, index=False, sheet_name='Selected Regular HH')
        selected_replacement.to_excel(writer, index=False, sheet_name='Selected Replacement HH')
        selected_appeal.to_excel(writer, index=False, sheet_name='Selected Appeal HH')
        rejected_hh.to_excel(writer, index=False, sheet_name='Rejected HH')

        # Protect each sheet with password2 to modify the file
        # workbook = writer.book
        # protect_options = {
        #     'workbook': False,
        #     'format_cells': False,
        #     'format_columns': False,
        #     'format_rows': False,
        #     'insert_columns': False,
        #     'insert_rows': False,
        #     'insert_hyperlinks': False,
        #     'delete_columns': False,
        #     'delete_rows': False,
        #     'select_locked_cells': True,
        #     'sort': False,
        #     'autofilter': False,
        #     'pivot_tables': False,
        #     'select_unlocked_cells': True,
        #     'objects': False,
        #     'scenarios': False,
        #     'copy': False,
        #     'print': False,
        #     'edit_objects': False,
        #     'edit_scenarios': False,
        # }

        # for worksheet in writer.sheets.values():
        #     worksheet.protect(password=password2, options=protect_options)

        # Close the writer to save the Excel file
        writer.close()
        output.seek(0)

        # Modify the file name by adding 'processed' suffix
        original_filename = excel_file.name
        filename, ext = os.path.splitext(original_filename)
        new_filename = f"{filename}_processed{ext}"

        # Return the file as an HTTP response
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="{new_filename}"'

        return response
    else:
        return render(request, 'upload_finalList.html')
