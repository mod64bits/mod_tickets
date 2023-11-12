from .models import Ticket
from bootstrap_modal_forms.forms import BSModalModelForm


class BookModelForm(BSModalModelForm):
    class Meta:
        model = Ticket
        fields = ['company', 'requester', 'department', 'description']