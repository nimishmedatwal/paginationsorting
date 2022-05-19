from django.shortcuts import render
from .models import Person
from django.core.paginator import Paginator
import json
# Create your views here.

def directory(request):
    # get_titles()  
    list=Person.objects.all().order_by('alphanumeric')
    paginator = Paginator(list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # return render(request, 'list.html', {'page_obj': page_obj})
    return render(request , "./page/directory.html", {'people' : page_obj} )

def get_titles():
    f = open('data.json')
    titles = json.load(f)
    for title in titles:
        Person.objects.create(name=title['name'],country=title['country'], region=title['region'],postalzip=title['postalZip'],phone=title['phone'],email=title['email'],address=title['address'],alphanumeric=title['alphanumeric'])

