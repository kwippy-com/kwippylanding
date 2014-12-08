import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.__init__ import login
from django.contrib.auth import authenticate
from miscproject.comingsoon.models import Beta_Invite
from django.template import Context, loader
from django.utils import simplejson
# Create your views here.

def coming_soon(request):
  if not request.method == "POST":
    return render_to_response('coming_soon.html',{})
  xhr = request.GET.has_key('xhr')
  response_dict = {}
  #user_ip = request.META['REMOTE_ADDR']
  user_ip = '127.0.0.1'
  user_email = request.POST.get('email',False)
  response_dict.update({'email':user_email})
  if user_email:
    new_beta = Beta_Invite(email = user_email, ip=user_ip)
    email_validate = new_beta.validate()
    if email_validate.has_key('email'):
      response_dict.update({'errors':'Email invalid'})
    else:
      new_beta.save()
      response_dict.update({'success':True})
  else:
    response_dict.update({'errors':'No email given'})
  if xhr:
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
  return render_to_response('coming_soon.html',response_dict)
