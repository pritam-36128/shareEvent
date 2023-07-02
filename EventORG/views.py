from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import path
from EventORG.services.notificationService import getLatestNotifications, createNotification
import json
from datetime import date
from .models.Notificaton import Notification 
from django.views.decorators.csrf import csrf_exempt

# this is a dic. containing sample data
events = {
        'event1': {
            'title': "event1",
            'description': "description-1"
        },
        'event2' : {
            'title': "event2",
            'description': "description-2"
        },
        'event3': {
            'title': "event3",
            'description': "description-3"
        },
        'event4' : {
            'title': "event4",
            'description': "description-4"
        }
    }
isActivated = False

# controller home page
def home(request):
    isActivated = False
    return render(request, "home.html")

# controller for rendering custom title and description
def shareEvent(request, eventID):
    isActivated = True
    return render(request, "home.html", {'isActivated': isActivated, 'event': events[eventID]})


# controller fro notifications
@csrf_exempt
def notifications_view(request):
    if request.method == 'GET': 
        try:
            # getLatestNotification is method to get latest notification 
            latestNotifications_json = json.dumps(list(getLatestNotifications().values()), default=str)
            response = HttpResponse(latestNotifications_json, content_type='application/json')
            return response
        except:
            return JsonResponse({'error': 'Something went wrong!'})

    elif request.method == 'POST':
        try:
            print("inside notification_view")

            # Retrieve JSON data from the request body
            json_data = json.loads(request.body)

            createNotification(json_data)
            # sending success message back to client
            return JsonResponse({'message': 'Entry created successfully'})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
                






