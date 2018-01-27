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
from models.RedisTokenManager import *

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
        return HttpResponse(q)
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


@csrf_exempt
def emailRegister(request):
    json_object = json.loads(json.dumps(request.POST))
    print(request.POST)
    verificationCode = json_object["verificationCode"]
    user_email = json_object["user_name"]
    if cache.get(user_email) != verificationCode:
        resp = {'error':1}
        return JsonResponse(json.dumps(resp), status=400,safe=False)
    cache.delete(user_email)
    if UserContact.objects.filter(user_email = user_email).count() > 0:
        resp = {'error': 2}
        return JsonResponse(json.dumps(resp), status=400, safe=False)
    serializer = SerializerUserInformation(data=json_object)
    if serializer.is_valid():
        user = serializer.save()
        user.usercontact.user_email = user.user_name
        user.usercontact.save()
        return JsonResponse({'error': 0}, status=201)
    return JsonResponse({'error':3}, status=400)

@csrf_exempt
def userLogin(request):
    json_object = json.loads(json.dumps(request.POST))
    userLoginname = json_object["user_name"]
    userPassword = json_object["user_password"]
    userContact = UserContact.objects.filter(Q(user_email = userLoginname) | Q(user_phone = userLoginname))
    if userContact.count == 0 or userContact[0].user.user_password != userPassword:
        return JsonResponse({"isLogged":"false"}, status = 401)
    else:
        tokenModel = RedisTokenManager.createToken(userContact[0].user.id)
        userInformation = []
        loginResult = {}
        loginResult["user_id"] = userContact[0].user.id
        loginResult["token"] = tokenModel.getToken()
        loginResult["user_name"] = userContact[0].user.user_name
        userInformation.append(loginResult)
        return JsonResponse({"userInformation":userInformation,"isLogged": "true"}, status=201)

@csrf_exempt
def emailVerification(request):
    json_object = json.loads(json.dumps(request.POST))
    email = json_object["user_email"]
    verificationCode, response = sendEmail(email)
    resp = {'verificationCode': verificationCode, 'response': response}
    return JsonResponse(resp, status = 201)

@csrf_exempt
def emailExist(request):
    json_object = json.loads(json.dumps(request.POST))
    email = json_object["user_email"]
    userContact = UserContact.objects.filter(user_email = email)
    resp = {'emailExist': userContact.count()}
    return JsonResponse(resp, status = 201)

@csrf_exempt
def tokenCheck(request):
    json_object = json.loads(json.dumps(request.POST))
    user_id = json_object["user_id"]
    token = json_object["token"]
    userTokenModel = TokenModel(int(user_id), token)
    isChecked = RedisTokenManager.checkToken(userTokenModel)
    resp = {"isChecked" : str(isChecked)}
    return JsonResponse(resp, status = 201)