from django.urls import path
from rr.views import *
app_name='rr'
urlpatterns=[
    path('sanju/',sanju,name='sanju'),
]