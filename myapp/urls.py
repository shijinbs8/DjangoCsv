from .views import *
from django.urls import path


urlpatterns=[

    path('upload-csv/',CsvReader.as_view(),name='upload-csv')
    
]