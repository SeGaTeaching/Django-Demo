from django.urls import path
from . import views

app_name = 'formapp'
urlpatterns = [
    path('', views.my_form, name='form'),
    path('strawhats/', views.create_strawhat, name='strawhat'),
    path('success', views.success, name='success')
]