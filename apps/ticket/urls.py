from django.urls import path
from .views import AdminListTicket, TicketCreateView

app_name = 'ticket'

urlpatterns = [
    path('', AdminListTicket.as_view(), name='list_ticket'),
    path('novo/', TicketCreateView.as_view(), name='new_ticket'),
]