from django.urls import path
from .views import AdminListTicket

app_name = 'ticket'

urlpatterns = [
    path('', AdminListTicket.as_view(), name='ticket_list'),
]