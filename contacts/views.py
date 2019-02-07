# Create your views here.
from .models import Contact


class ContactList(ListView):
    model = Contact
