from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client


def sms(request):
    account_sid = 'ACba8dd66ac66856bde921aa4268cd2a84'
    auth_token = '031e0ba47b92a90f81fd141627a62b4f'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_='+12184232326',
                         to='+917389944161'
                     )
    return HttpResponse("messages sent!", 200)
