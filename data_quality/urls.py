from django.urls import path
from . import views

app_name = 'data_quality'  # replace 'data_quality' with your actual app name

urlpatterns = [
    path('', views.index, name='index'),
    path('create-df/', views.create_df, name='create-df'),
    path('import-data/', views.ImportDataView.as_view(), name='dqa'),
    path('dqa_analysis/', views.dqa_analysis, name='dqa_analysis'),
]