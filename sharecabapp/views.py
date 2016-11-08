from django.shortcuts import render_to_response
from django.template.context import RequestContext
from sharecabapp.models import Ride
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    new_ride.name= request.user
    new_ride.ridetime = d['time']
    new_ride.ridedate = d['date']
    new_ride.email = d['email']
    new_ride.source = d['source']
    new_ride.destination = d['destination']
    new_ride.train = d['train']
    new_ride.preference = d['preference']
    new_ride.save()
    return render_to_response('thanks.html')


def thankyou(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('thankyou.html',
                             context_instance=context)

def result(request):
    queryRes = Ride()
    d = request.POST
    if len(Ride.objects.filter(train__exact = d['train'])) > 0 :
        queryRes = Ride.objects.filter(train__exact = d['train'])

    return render_to_response('display.html',{ 'answer': queryRes })

def profile(request):
    queryRes = Ride()
    if len(Ride.objects.filter(name__exact = request.user)) > 0 :
        queryRes = Ride.objects.filter(name__exact = request.user)
    return render_to_response('display.html',{ 'answer': queryRes })


def review(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('review.html',
                             context_instance=context)
