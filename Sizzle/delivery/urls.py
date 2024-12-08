from django.urls import path, include
from . import views
app_name = 'delivery'
urlpatterns = [
    path('deliveryhomepage/', views.deliveryhomepage, name='deliveryhomepage'),
    ]
