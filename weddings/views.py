from django.shortcuts import render
from django.http import HttpResponse
from .models import Wedding
from .models import Supplier

# Create your views here.

def index(request):
    """The view for the welcome page of the app"""

    # Generation of some statistical objects for the main page
    num_weddings = Wedding.objects.all().count()

    # Here will be the count of upcoming and past weddings
    num_suppliers = Supplier.objects.all().count()

    # Count the nubmer of visits
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
    'num_weddings': num_weddings,
    'num_suppliers': num_suppliers,
    'num_visits': num_visits,
    }

    # render the HTML data with the data in some context variable

    return render(request, 'index.html', context=context)

# The home page of each user where you can navigate to the all functions of the web_site

def home(request):
    """The users home page"""

    return render(request, 'home.html')
