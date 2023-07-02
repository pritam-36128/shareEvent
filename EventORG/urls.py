from django.contrib import admin
from django.urls import path
from .views import notifications_view, home, shareEvent



#  router mapping
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('domain/share/<str:eventID>/', shareEvent, name='shareEvent'),
    path('getnotifications/', notifications_view),
    path('notifications/', notifications_view)
]

