from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'restaurant'
urlpatterns = [
    path('restauranthomepage/', views.restauranthomepage, name='restauranthomepage'),
    path('rrdarbar/', views.rrdarbar, name='rrdarbar'),
    ]