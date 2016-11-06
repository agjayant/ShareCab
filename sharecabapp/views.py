from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)

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

