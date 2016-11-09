from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from sharecabapp.models import Ride,Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from django.core.context_processors import csrf

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

def ridepage(request,id ):
    comments = Comment()
    if len(Comment.objects.filter(rideNum__exact = id )) > 0:
        comments = Comment.objects.filter(rideNum__exact = id )
    c = {'answer': comments, 'id': id }
    c.update(csrf(request))
    return render_to_response('comments.html',c)

def addComment(request ):
    newComment = Comment()
    d = request.POST
    thisRide = Ride.objects.get(id__exact = d['id'] )
    newComment.rideNum = thisRide
    newComment.name = request.user.first_name
    newComment.comment = d['comment']
    newComment.commentTime = datetime.datetime.now()
    newComment.save()

    comments = Comment()
    if len(Comment.objects.filter(rideNum__exact = thisRide )) > 0:
        comments = Comment.objects.filter(rideNum__exact = thisRide )
    c = {'answer': comments ,'id': d['id'] }
    return render(request, 'comments.html', c )


def review(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('review.html',
                             context_instance=context)
