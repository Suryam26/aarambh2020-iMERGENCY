from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings

url=settings.CURRENT_URL

def home(request):
    return render(request,'index.html',{'url':url, 'emergency': 0, 'reached': 0})


def sms(request):
    account_sid = 'ACba8dd66ac66856bde921aa4268cd2a84'
    auth_token = 'cbdfc15fd8141b6c237963a3dbc9a935'
    client = Client(account_sid, auth_token)
    lat = request.GET['lat']
    lng = request.GET['lng']
    type = request.GET['type']
    message = client.messages.create(
                         body="http://maps.google.com/maps?q="+lat+","+lng,
                         from_='+12184232326',
                         to='+917389944161'
                     )
    if type == '1':
        return render(request,'index.html',{'url':url, 'emergency': 1, 'reached': 0})

    if type == '2':
        return render(request,'index.html',{'url':url, 'emergency': 0, 'reached': 1})
