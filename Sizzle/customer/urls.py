from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Order
from . import views
app_name='customer'
urlpatterns = [
    path('', views.homepage, name='HomePage'),
    path('MainPage/', views.MainPage, name='MainPage'),
    path('SignUpLogic/', views.SignUpLogic, name='SignUpLogic'),
    path('SignUpCall/', views.SignUpCall, name='SignUpCall'),
    path('SignInCall/', views.SignInCall, name='SignInCall'),
    path('SignInLogic/', views.SignInLogic, name='SignInLogic'),
    path('SignOut/', views.SignOut, name='SignOut'),
    path('choosing/',views.choosing,name='choosing'),
    path('home123/',views.home123,name='home123'),
    path('order/',Order.as_view(), name='order'),
    path('Online/',views.Online, name='Online'),
    path('Cash/',views.Cash,name='Cash'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


