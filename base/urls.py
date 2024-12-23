from django.urls import path
from . import views
from . import final_list_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    # path('dqa/', views.dqa, name='dqa'),
    path('import_data/', views.import_data, name='import_data'),
    path('error_check/', views.error_check, name='error_check'),
    path('final_list/', views.final_list, name='final_list'),
    path('final_list_report/', views.final_list_report, name='final_list_report'),
    path('reports/', views.reports, name='reports'),
    path('media_upload/', views.upload_media, name='media_upload'),
    path('upload_sample/', views.upload_sample_to_moda, name='upload_sample'),
    path('moda_user_mgt/', views.moda_user_mgt, name='moda_user_mgt'),
    path('import-csv/', views.CSVImportView.as_view(), name='csv_import'),
    path('import-tpm-csv/', views.TPMCSVImportView.as_view(), name='import_tpm_csv'),
    path('import-tpm-ee-csv/', views.TPMEEVImportView.as_view(), name='import_tpm_ee_csv'),
    path('drop_records/', views.CSVImportViewDropRecords.as_view(), name='drop_records'),
    
    path('sampling/', views.sampling, name='sampling'),
    path('est_sample/', views.CSVDataCountView.as_view(), name='est_sample'),
    path('generate_sample/', views.GenerateSampleView.as_view(), name='generate_sample'),
    path('approve_sample/', views.ApproveSampleView.as_view(), name='approve_sample'),
    path('sampling_report/', views.sampling_report, name='sampling_report'),
    path('sample_report/', views.SampleViewReport.as_view(), name='sample_report'),
    
    
    path('sampling_borderline/', views.sampling_borderline, name='sampling_borderline'),
    path('est_borderline_sample/', views.SampledLocations_bordeline.as_view(), name='est_borderline_sample'),
    # path('est_sample_borderline/', views.CSVDataCountViewBorderline.as_view(), name='est_sample_borderline'),
    path('gen_borderline_sample/', views.GenerateRandomSites.as_view(), name='gen_borderline_sample'),
    # path('approve_sample/', views.ApproveSampleView.as_view(), name='approve_sample'),
    
    path('custom_sampling_borderline/', views.custom_sampling_borderline, name='custom_sampling_borderline'),
    path('est_custom_borderline_sample/', views.SampledLocations_bordeline_custom.as_view(), name='est_custom_borderline_sample'),
    # path('est_sample_borderline/', views.CSVDataCountViewBorderline.as_view(), name='est_sample_borderline'),
    path('gen_custom_borderline_sample/', views.GenerateRandomSites_custom.as_view(), name='gen_custom_borderline_sample'),
    
    path('filal_list_locations/', views.SampledLocations.as_view(), name='filal_list_locations'),
    path('final_list_data_analysis/', views.FinalListDataAnalysis.as_view(), name='final_list_data_analysis'),
    path('final_list_data_analysis_report/', views.FinalListDataAnalysisReport.as_view(), name='final_list_data_analysis_report'),
    path('check_keys_in_excel/', views.check_keys_in_excel, name='check_keys_in_excel'),
    path('summary_view/', views.summary_view.as_view(), name='summary_view'),
    
    path('export/<str:model_name>/', views.export_model_to_excel, name='export_model_to_excel'),
    
    
    # test final views.
    path('final_list_test/', final_list_views.DataCountsGroupedView.as_view(), name='final_list_test'),
    # path('test_view_final_approval/', views.test_view_final_approval, name='final_list_test2'),
    path('test_view_final_approval/', views.FinalListApproval.as_view(), name='final_list_test3'),
    
    
    
]
