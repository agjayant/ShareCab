from django.shortcuts import render_to_response
from django.template.context import RequestContext
from sharecabapp.models import Ride
from django.contrib.auth.decorators import login_required

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)

# @login_required(login_url="/home/")
def insert(request):

   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('insert.html',
                             context_instance=context)

def query(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('query.html',
                             context_instance=context)

def entry(request):
    new_ride = Ride()
    d = request.POST
    new_ride.name= d['name']
    new_ride.ridetime = d['time']
    new_ride.email = d['email']
    new_ride.source = d['source']
    new_ride.destination = d['destination']
    new_ride.train = d['train']
    new_ride.capacity = d['capacity']
    new_ride.preference = d['preference']
    new_ride.save()
    return render_to_response('thankyou.html')


def thankyou(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('thankyou.html',
                             context_instance=context)

def display(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('display.html',
                             context_instance=context)


def result(request):
    queryRes = Ride()
    d = request.POST
    if len(Ride.objects.filter(train__exact = d['train'])) > 0 :
        queryRes = Ride.objects.filter(train__exact = d['train'])

    return render_to_response('display.html',{ 'answer': queryRes })



