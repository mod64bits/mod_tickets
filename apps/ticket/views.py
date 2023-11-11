from django.shortcuts import render

from django.views.generic.list import ListView
from .models import Ticket


class AdminListTicket(ListView):
    model = Ticket
    template_name = 'ticket/ticket_admin_ticket.html'
