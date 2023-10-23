from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.urls import reverse

# Create your views here.
def homePageView(request):
  return HttpResponse('<h1>Home Page</h1>')

def aboutPageView(request):
  #var = {'var1':1, 'var2':[1,2,3], 'var3':range(1,6)} 
  #today = datetime.datetime.now().date()
  #daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  #dicts = {'a':0, 'b':1}
  #context = {"today" : today, "days_of_week" : daysOfWeek, 'dicts':dicts}
  #context = {'var': var, "today": today}
  # For Tag: Loop Through a Range
  years = list(range(2020, 2023))
  # If Tag: Conditional Rendering
  is_vision_clear = True
  # Empty Tag: Check if a Variable is Empty
  team_members = ['a','b'] 
  
  context = {'years': years,'is_vision_clear': is_vision_clear,
             'team_members': team_members, 'a':'<b>Hello<b>'}
  return render(request, 'about.html', context)
  #return render(request, 'about.html')

def articlePageView(request, id):
  return HttpResponse(f'<h1>Article {id}</h1>')

def search(request, keyword, id):
  return HttpResponse(f'search for keyward {keyword} and id {id}')
  #return redirect(date, year = "2045", month = "02", slug = "test")
  #return redirect(reverse('about'))

def date(request, year, month, slug):
  #print(request.GET.get('a'))
  return HttpResponse(f'Date:{year}-{month} with title:{slug}')

def filterView(request):
  some_date = datetime.date(2023, 4, 15)
  some_time = datetime.time(14, 30)
  future_date = datetime.date(2023, 12, 1)
  past_date = datetime.date(2023, 1, 15)
  some_list = ["Item 1", "Item 2", "Item 3"]
  some_dict = {"a":1, "b":2, "c":['x','y','z']}

  context = {
    'some_date': some_date,
    'some_time': some_time,
    'future_date': future_date,
    'past_date': past_date,
    'some_list': some_list,
    'some_dict': some_dict,
    }
  
  return render(request, 'filter_example.html', context)