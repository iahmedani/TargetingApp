from django.urls import path
from . import views

app_name = 'media_files'

urlpatterns = [
    path('', views.home, name='media_home'),
    path('upload_province/', views.uploadProvince, name='upload_province'),
    path('upload_district/', views.uploadDistrict, name='upload_district'),
    path('upload_tpm/', views.uploadTPM, name='upload_tpm'),
    path('upload_cp/', views.uploadCP, name='upload_cp'),
    path('upload_cfac/', views.uploadCFAC, name='upload_cfac'),
    path('upload_villages/', views.uploadVillages, name='upload_villages'),
    path('upload_sample/', views.uploadSampleToMoDa, name='upload_sample'),
    path('user_access/', views.update_user_access, name='user_access'),
]
