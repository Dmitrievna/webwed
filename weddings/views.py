from django.shortcuts import render
from django.http import HttpResponse
from .models import Wedding
from .models import Supplier
from rest_framework.decorators import api_view
from .forms import WeddingForm

# Create your views here.

def home(request):
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

    return render(request, 'home.html', context=context)

def base(request):
    #Check how base thing works
    return render(request, 'base_generic.html')

def get_wedding(request):

    if request.method == 'POST':
        form = WeddingForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/home/')
    else:
        form = WeddingForm()

    return render(request, 'get_wedding.html', {'form': form})
