# Create your views here.
from .models import Contact


class ContactList(ListView):
    model = Contact


class ContactDetail(DetailView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact


class ContactUpdate(UpdateView):
    model = Contact
