from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def about(request):  # Add this new view function
    return render(request, 'pages/about.html')

def services(request):  # Add this new view function
    return render(request, 'pages/services.html')
def contact(request):  # view for contact
    return render(request, 'pages/contact.html')
def cars(request):  # view for cars
    return render(request, 'pages/cars.html')
def contact(request):  # view for contact
    return render(request, 'pages/contact.html')
def login(request):  # view for login
    return render(request, 'pages/login.html')
def signup(request):  # view for signup
    return render(request, 'pages/signup.html')

def dashboard(request):  # view for dashboard
    return render(request, 'pages/dashboard.html')
