from django.urls import path
from . import views

app_name = 'websites'

urlpatterns=[
    path('',views.my_form,name="add_website"),
    
    
]

