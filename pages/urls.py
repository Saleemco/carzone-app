from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('services.html', views.services, name='services'),
    path('cars.html', views.cars, name='cars'),
    
    path('contact.html', views.contact, name='contact'),
    path('login.html', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    
]