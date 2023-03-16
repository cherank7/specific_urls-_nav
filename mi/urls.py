from django.urls import path
from mi.views import *
app_name='mi'
urlpatterns=[
    path('rohith/',rohith,name='rohith'),
]