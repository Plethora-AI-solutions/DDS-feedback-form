from django.urls import path
from feedback_form import views



urlpatterns = [
    path('', views.index, name='index'), 
    path('form_submit', views.form_submit, name='form_submit'),
  
]