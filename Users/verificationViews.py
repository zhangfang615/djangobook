from django.http import Http404, HttpResponse, JsonResponse
import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from tools.emailSending import *
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Users.serializers import  *
from Users.models import *
from django.db.models import Q

def emailVerification(request, email):
    try:
        email = str(email)
    except ValueError:
        raise Http404
    verificationCode, response = sendEmail(email)
    resp = {'verificationCode': verificationCode, 'response': response}

    return HttpResponse(json.dumps(resp), content_type="application/json")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def gettest(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return  HttpResponse(q)
    else:
        return HttpResponse('Please submit a get term.')

@csrf_exempt
def phoneRegister(request):
    json_object = json.loads(json.dumps(request.POST))
    serializer = SerializerUserInformation(data=json_object)
    if serializer.is_valid():
        user = serializer.save()
        user.usercontact.user_phone = user.user_name
        user.usercontact.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
    # print("connected")
    # if request.POST.get('userPhone'):
    #     q = request.POST['userPhone']
    #     resp = {'userPhone': str(q), 'response': "done"}
    # else:
    #     resp = {'userPhone': "unknown", 'response': "notdone"}
    # return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def emailRegister(request):
    json_object = json.loads(json.dumps(request.POST))
    serializer = SerializerUserInformation(data=json_object)
    if serializer.is_valid():
        user = serializer.save()
        user.usercontact.user_email = user.user_name
        user.usercontact.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def userLogin(request):
    json_object = json.loads(json.dumps(request.POST))
    userLoginname = json_object["user_name"]
    userPassword = json_object["user_password"]
    userContact = UserContact.objects.filter(Q(user_email = userLoginname) | Q(user_phone = userLoginname))
    if userContact.count == 0 or userContact[0].user.user_password != userPassword:
        return JsonResponse({"isLogged":"false"}, status = 401)
    else:
        return JsonResponse({"isLogged": "true"}, status=201)