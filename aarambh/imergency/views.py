from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings

# Base URL
url=settings.CURRENT_URL


# Home Page
def home(request):
    return render(request,'index.html',{'url':url, 'emergency': 0, 'reached': 0})


# Sending Messages
def sms(request):
    # Messaging API (We are using a trial version of this API for development purposes)
    account_sid = 'ACba8dd66ac66856bde921aa4268cd2a84'
    auth_token = '392d6ee158aa8a7e54f84895470eeee2'     #This Token changes within 24hrs
    client = Client(account_sid, auth_token)


    # Extracting data from GET request
    lat = request.GET['lat']
    lng = request.GET['lng']
    name = request.GET['name']
    phn1 = request.GET['phn1']
    phn2 = request.GET['phn2']
    phn3 = request.GET['phn3']
    type = request.GET['type']

    # Creating an array of phone numbers
    phoneNo = []
    if phn1 and len(phn1)>10: phoneNo.append(phn1.replace(" ", "+"))
    if phn2 and len(phn2)>10: phoneNo.append(phn2.replace(" ", "+"))
    if phn3 and len(phn3)>10: phoneNo.append(phn3.replace(" ", "+"))


    # For "Emergency"
    if type == '1':
        phoneNo.append("+100")     #Adding phone-number of authority
        msgBody = "\n\nEMERGENCY!!! \nThis is " + name + ". \nI need HELP! \nThis is my current location: \nhttp://maps.google.com/maps?q="+lat+","+lng
        message = client.messages.create(
                             body= msgBody,
                             from_='+12184232326',
                             to='+917389944161'        #In trial version we can only send messages to one fixed number.
                         )

        message = client.messages.create(
                              body= msgBody,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+917389944161'       #In trial version we can only send messages to one fixed number.
                          )

        # In the full version of this API we can send messages to more then one person at a time by passing in an array of numbers
        # Sample code:
                # message = client.messages.create(
                #                       body= msgBody,
                #                       from_='whatsapp:+14155238886',
                #                       to= phoneNo
                #                   )


        return render(request,'index.html',{'url':url, 'emergency': 1, 'reached': 0})


    # For "On my way"
    if type == '2':
        msgBody = "\n\nThis is " + name + ". \nI am on my way. \nThis is my current location: \nhttp://maps.google.com/maps?q="+lat+","+lng
        message = client.messages.create(
                             body= msgBody,
                             from_='+12184232326',
                             to='+917389944161'     #In trial version we can only send messages to one fixed number.
                         )

        message = client.messages.create(
                              body= msgBody,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+917389944161'       #In trial version we can only send messages to one fixed number.
                          )
        return render(request,'index.html',{'url':url, 'emergency': 0, 'reached': 1})
