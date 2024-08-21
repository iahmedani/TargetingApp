import pandas as pd
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from dtale.views import startup
import io
import dtale.global_state as global_state
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