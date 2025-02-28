from django.urls import path
from . import views

app_name = 'demoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name="qryview"),
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
    path('math/<num1>/<num2>/', views.math, name='math'),
]
