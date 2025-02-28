from django.urls import path
from . import views

app_name = 'mangaform'
urlpatterns = [
    path('', views.overview),
    path('add/', views.submit_manga, name='manga'),
    path('success/', views.success, name='success'),
]
