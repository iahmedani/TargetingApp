from django.urls import path
from . import views

app_name = 'data_quality'  # replace 'data_quality' with your actual app name

urlpatterns = [
    path('', views.index, name='index'),
    path('create-df/', views.create_df, name='create-df'),
    path('import-data/', views.ImportDataView.as_view(), name='dqa'),
    path('dqa_analysis/', views.dqa_analysis, name='dqa_analysis'),
    path('excel_upload_view/', views.excel_upload_view, name='excel_import'),
    path('std_data_analysis/', views.std_data_analysis, name='analyze_data'),
    path('cfac_excel_upload_view/', views.cfac_excel_upload_view, name='cfac_excel_import'),
    path('cfac_village_list_prep/', views.process_excel_file, name='cfac_village_list_prep'),
    path('deduplicate_upload/', views.deduplicate_upload, name='deduplicate_upload'),
    path('deduplicate_export/', views.deduplicate_export, name='deduplicate_export'),
    path('compare_files/', views.compare_excel_documents, name='compare_files'),
    path('prepare_final_list/', views.prepare_final_list, name='prepare_final_list')
]