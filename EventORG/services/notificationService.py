from ..models.Notificaton import Notification


def getLatestNotifications():
    notifications = Notification.objects.filter(sent=False)
    return notifications


def createNotification(json_data):
    # Extract the necessary data from the JSON
    eid = json_data.get('eid')
    message = json_data.get('message')
    sent = json_data.get('sent')

    # creating Notification object and initializing 
    notification = Notification()
    notification.eid: int = eid
    notification.message: str = message
    notification.sent: bool = sent
    # saving object in database
    notification.save()