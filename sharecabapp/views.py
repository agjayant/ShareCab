from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from sharecabapp.models import Ride,Comment,Driver, Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from django.core.context_processors import csrf
from django.db.models import Avg

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

def update(request):
    new_ride = Ride()
    d = request.POST
    new_ride.name= request.user
    new_ride.ridetime = d['time']
    new_ride.ridedate = d['date']
    # new_ride.email = d['email']
    new_ride.source = d['source']
    new_ride.destination = d['destination']
    new_ride.train = d['train']
    new_ride.preference = d['preference']
    new_ride.save()
    # return render_to_response('thanks.html')

    queryRes = Ride()
    if len(Ride.objects.filter(name__exact = request.user)) > 0 :
        queryRes = Ride.objects.filter(name__exact = request.user)
    return render_to_response('yourRides.html',{ 'answer': queryRes })



def thankyou(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('thankyou.html',
                             context_instance=context)

def result(request):
    queryRes = Ride()
    d = request.POST
    time1 = d['time1']
    time2 = d['time2']

    if len(Ride.objects.filter(train__exact = d['train'] , ridedate__exact = d['date']) ) > 0 :
        queryRes = Ride.objects.filter(train__exact = d['train'] , ridedate__exact = d['date'])
    elif len (Ride.objects.filter(source__exact = d['source'] , destination__exact = d['destination'] , ridedate__exact = d['date'] , ridetime__gte = time1 , ridetime__lte = time2)) > 0 :
        queryRes = Ride.objects.filter(source__exact = d['source'] , destination__exact = d['destination'] , ridedate__exact = d['date'] ).order_by('ridetime')

    return render_to_response('display.html',{ 'answer': queryRes })

def profile(request):
    queryRes = Ride()
    if len(Ride.objects.filter(name__exact = request.user)) > 0 :
        queryRes = Ride.objects.filter(name__exact = request.user)
    return render_to_response('yourRides.html',{ 'answer': queryRes })

def drivers(request):
    queryRes = Driver.objects.all()
    return render_to_response('drivers.html',{ 'answer': queryRes })

def drivReviews(request, mobile):
    thisDriver = Driver.objects.get(mobile__exact = mobile)
    allReviews = Review.objects.filter(driverNum__exact = thisDriver )
    c= {'answer': allReviews , 'driv': thisDriver}
    return render_to_response('driverReviews.html',c)



def delete(request,id):
    Ride.objects.filter( id__exact = id ).delete()

    queryRes = Ride()
    if len(Ride.objects.filter(name__exact = request.user)) > 0 :
        queryRes = Ride.objects.filter(name__exact = request.user)
    return render_to_response('yourRides.html',{ 'answer': queryRes })

def edit(request,id):
    # Ride.objects.filter( id__exact = id ).delete()

    # queryRes = Ride()
    # if len(Ride.objects.filter(name__exact = request.user)) > 0 :
        # queryRes = Ride.objects.filter(name__exact = request.user)

    queryRes = Ride.objects.get( id__exact = id )

    Ride.objects.filter( id__exact = id ).delete()
    c = {'answer' : queryRes }
    c.update(csrf(request))
    return render_to_response('edit.html',c)


# def ridepage(request,id ):
#     comments = Comment()
#     if len(Comment.objects.filter(rideNum__exact = id )) > 0:
#         comments = Comment.objects.filter(rideNum__exact = id )
#     c = {'answer': comments, 'id': id }
#     c.update(csrf(request))
#     return render_to_response('comments.html',c)

def ridepage(request,id ):
    comments = Comment()
    if len(Comment.objects.filter(rideNum__exact = id )) > 0:
        comments = Comment.objects.filter(rideNum__exact = id )
    thisRide = Ride.objects.get(id__exact = id )
    c = {'answer': comments, 'id': id, 'ridedetails':thisRide}
    c.update(csrf(request))
    return render_to_response('comindex.html',c)


# def addComment(request ):
#     newComment = Comment()
#     d = request.POST
#     thisRide = Ride.objects.get(id__exact = d['id'] )
#     newComment.rideNum = thisRide
#     newComment.name = request.user.first_name
#     newComment.comment = d['comment']
#     newComment.commentTime = datetime.datetime.now()
#     newComment.save()

#     comments = Comment()
#     if len(Comment.objects.filter(rideNum__exact = thisRide )) > 0:
#         comments = Comment.objects.filter(rideNum__exact = thisRide )
#     c = {'answer': comments ,'id': d['id'] }
#     return render(request, 'comments.html', c )

def addComment(request ):
    newComment = Comment()
    d = request.POST
    thisRide = Ride.objects.get(id__exact = d['id'] )
    newComment.rideNum = thisRide
    newComment.name = request.user.first_name
    newComment.comment = d['comment']
    newComment.commentTime = datetime.datetime.now()
    newComment.save()
    #Comment.objects.order_by(commentTime.asc())
    comments = Comment()
    if len(Comment.objects.filter(rideNum__exact = thisRide )) > 0:
        comments = Comment.objects.filter(rideNum__exact = thisRide )
    c = {'answer': comments ,'id': d['id'], 'ridedetails':thisRide}
    return render(request, 'comindex.html', c )


def review(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('review.html',
                             context_instance=context)

def rating(request):
    driver = Driver()
    d = request.POST
    if len(Driver.objects.filter(mobile__exact = d['mobile'])) == 0:
        driver.userName = request.user
        driver.vehicleNum = d['vehicleNo']
        driver.driverName = d['name']
        driver.mobile = d['mobile']
        driver.avgRating = d['rating']
        driver.save()

    reveiw = Review()
    reveiw.driverNum = Driver.objects.get(mobile__exact = d['mobile'])
    reveiw.userName = request.user
    reveiw.comment = d['comment']
#    reveiw.commentTime = d['date']
    reveiw.date = d['date']
    reveiw.rating = d['rating']
    reveiw.save()

#    Driver.objects.filter(mobile__exact = d['mobile']).update(avgRating= (Review.objects.filter(driverNum__exact = d['mobile']).aggregate(Avg('rating')) ))

    return render_to_response('thanks.html')
