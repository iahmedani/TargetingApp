import pandas as pd
import os
from io import BytesIO

def load_excel_file(file_path):
    """Load the Excel file into a DataFrame."""
    df = pd.read_excel(file_path)
    return df

def clean_dataframe(df):
    """Clean column names and strip whitespace from string data."""
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

def check_required_columns(df, required_columns):
    """Check if the required columns are present in the DataFrame."""
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        return False, missing_columns
    return True, None

def ensure_remarks_column(df):
    """Ensure that the 'Remarks' column exists and is of string type."""
    if 'Remarks' not in df.columns:
        df['Remarks'] = ''
    else:
        df['Remarks'] = df['Remarks'].fillna('').astype(str)
    return df

def map_province_and_district_codes(df, province_file, district_file):
    """Map province and district codes from provided CSV files."""
    province = pd.read_csv(province_file)
    district = pd.read_csv(district_file)

    # Clean and prepare the province and district data
    province['label'] = province['label'].str.strip().str.title()
    district['label'] = district['label'].str.strip().str.title()
    df['Province'] = df['Province'].str.strip().str.title()
    df['District'] = df['District'].str.strip().str.title()

    # Merge province codes
    df = df.merge(province[['label', 'name']], left_on='Province', right_on='label', how='left')
    df.rename(columns={'name': 'Province_code'}, inplace=True)
    df.drop(columns=['label'], inplace=True)

    # Merge district codes
    df = df.merge(district[['label', 'name']], left_on='District', right_on='label', how='left')
    df.rename(columns={'name': 'District_code'}, inplace=True)
    df.drop(columns=['label'], inplace=True)

    return df

def add_remarks_for_missing_codes(df):
    """Add remarks for rows with missing province or district codes."""
    missing_codes = df['Province_code'].isnull() | df['District_code'].isnull()
    df.loc[missing_codes, 'Remarks'] += 'Unable to map province and/or district codes. '
    return df

def check_missing_focal_point_contacts(df):
    """Check for missing focal point contact numbers and add remarks."""
    valid_codes = df['Province_code'].notnull() & df['District_code'].notnull()
    missing_contacts = df['FP1 Number'].isnull() & df['FP2 Number'].isnull()
    df.loc[valid_codes & missing_contacts, 'Remarks'] += 'At least one focal point should have a contact number. '
    return df

def create_cfac_codes(df, is_urban):
    """Create CFAC codes for urban or rural areas."""
    df['CFAC Name'] = df['CFAC Name'].str.title()
    if is_urban:
        df['CFAC_Code'] = df['District_code'].astype(str) + "_PD_" + df['Nahia'].astype(str) + "_" + df['CFAC Name']
    else:
        df['CFAC_Code'] = df['District_code'].astype(str) + "_" + df['CFAC Name']
    return df

def create_cfac_list(df):
    """Create CFAC list DataFrame."""
    cfac_list = pd.DataFrame({
        'list_name': 'cfac_list',
        'name': df['CFAC_Code'],
        'label': df.apply(lambda x: f"PD {x['Nahia']} {x['CFAC Name']}" if x['Area'] == 'Urban Area' else x['CFAC Name'], axis=1),
        'ao': df['AO'],
        'province': df['Province'],
        'district': df['District'],
        'CFAC_FP1': df['CFAC FP 1'],
        'FP1_Number': df['FP1 Number'],
        'CFAC_FP2': df['CFAC FP2'],
        'FP2_Number': df['FP2 Number'],
        'Province_code': df['Province_code'],
        'District_code': df['District_code'],
        'CFAC_Name': df['CFAC Name'],
    }).drop_duplicates()
    return cfac_list

def create_village_codes(df, is_urban):
    """Create village codes for urban or rural areas."""
    df['Village'] = df['Village'].str.title()
    if is_urban:
        df['cfac_code'] = df['District_code'].astype(str) + "_PD_" + df['Nahia'].astype(str) + "_" + df['CFAC Name']
        df['village_code'] = df['cfac_code'] + "_" + df['Village']
    else:
        df['cfac_code'] = df['District_code'].astype(str) + "_" + df['CFAC Name']
        df['village_code'] = df['cfac_code'] + "_" + df['Village']
    return df

def create_village_list(df):
    """Create village list DataFrame."""
    village_list = pd.DataFrame({
        'list_name': 'village_list',
        'name': df['village_code'],
        'label': df['Village'],
        'cfac_code': df['cfac_code'],
        'Province': df['Province'],
        'District': df['District'],
        'Province_code': df['Province_code'],
        'District_code': df['District_code'],
        'CFAC_Name': df['CFAC Name'],
        'ao': df['AO'],
    }).drop_duplicates()
    return village_list

def save_to_excel(df_dict, output_file):
    """Save DataFrames to an Excel workbook."""
    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, df in df_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
