from django.urls import reverse_lazy
from .forms import BookModelForm
from bootstrap_modal_forms.generic import BSModalCreateView

from django.views.generic.list import ListView
from .models import Ticket


class AdminListTicket(ListView):
    model = Ticket
    template_name = 'ticket/ticket_admin_ticket.html'


class TicketCreateView(BSModalCreateView):
    template_name = 'ticket/create_ticket.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ticket:list_ticket')


