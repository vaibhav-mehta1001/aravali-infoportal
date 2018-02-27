from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from InfoPortal.authhelper import get_signin_url
from InfoPortal.outlookservice import get_me
from InfoPortal.authhelper import get_token_from_code
from InfoPortal.outlookservice import get_me
from InfoPortal.authhelper import get_signin_url, get_token_from_code, get_access_token
from . import models
from django.contrib.auth.decorators import login_required
import time
from django.utils.decorators import method_decorator
from django.views import generic

# Admin Password tsrsadmin

# Create your views here.
def home(request):
 try:
   logoff = request.session['logoff']
 except KeyError:
     access_token = ''
     redirect_uri = request.build_absolute_uri(reverse('InfoPortal:landing'))
     sign_in_url = get_signin_url(redirect_uri)
     context = { 'signin_url': sign_in_url }
     return render(request, 'InfoPortal/index.html', context)
 if logoff is True :
     access_token = ''
     redirect_uri = request.build_absolute_uri(reverse('InfoPortal:landing'))
     sign_in_url = get_signin_url(redirect_uri)
     context = { 'signin_url': sign_in_url }
     return render(request, 'InfoPortal/index.html', context)
 elif logoff is False:
     return HttpResponseRedirect(reverse('InfoPortal:main'))

  #return HttpResponse('<a href="' + sign_in_url +'">Click here to sign in and view your mail</a>')
def landing(request):
  
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('InfoPortal:landing'))
  token = get_token_from_code(auth_code, redirect_uri)
  access_token = token['access_token']
  user = get_me(access_token)
  refresh_token = token['refresh_token']
  expires_in = token['expires_in']

  # expires_in is in seconds
  # Get current timestamp (seconds since Unix Epoch) and
  # add expires_in to get expiration time
  # Subtract 5 minutes to allow for clock differences
  expiration = int(time.time()) + expires_in - 300

  # Save the token in the session
  request.session['access_token'] = access_token
  request.session['refresh_token'] = refresh_token
  request.session['token_expires'] = expiration
  request.session['user_email'] = user['mail']
  user_email = user['mail']
  request.session['logoff'] = True
  if user_email is not None:
    if user_email.find("tsrs.org") == -1:
          return HttpResponseRedirect(reverse('InfoPortal:logout'))
    else:
     request.session['logoff'] = False
     return HttpResponseRedirect(reverse('InfoPortal:main'))
  else: 
    return HttpResponseRedirect(reverse('InfoPortal:home'))
  
def main(request):

 queryset = models.Entry.objects.published().order_by('-created')
 template_name = 'InfoPortal/main.html'
 page = request.GET.get('page', 1)
 paginator = Paginator(queryset, 10)
 try:
    posts = paginator.page(page)
 except PageNotAnInteger:
    posts = paginator.page(1)
 except EmptyPage:
    posts = paginator.page(paginator.num_pages)
 try:
  logoff = request.session['logoff']
 except KeyError:
    return HttpResponseRedirect(reverse('InfoPortal:home'))
 if logoff is False :
   access_token = get_access_token(request, request.build_absolute_uri(reverse('InfoPortal:landing')))
   # user_email = user['mail']
   #access_token =request.session['access_token']
   # context = { 'user_email': user_email }
   # If there is no token in the session, redirect to home
   if not access_token:
    request.session['logoff'] = True
    return HttpResponseRedirect(reverse('InfoPortal:logout'))
   else:
      return render(request, 'InfoPortal/main.html', { 'posts': posts })
 else:
  return HttpResponseRedirect(reverse('InfoPortal:home'))

def  logout(request):
   #access_token = 'randomstuff'
  request.session['logoff'] = True
  request.session['access_token'] = 'invalid'
  return HttpResponseRedirect("https://login.microsoftonline.com/common/oauth2/logout?post_logout_redirect_uri=https://login.microsoftonline.com/")
 
 

  
 
  
