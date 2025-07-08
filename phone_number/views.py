from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from phone_number.models import Contact


# Create your views here.


class ListContact(ListView):
    """
    show list of all  contacts on login account
    """
    model = Contact
    context_object_name = 'contacts'
    template_name = 'phone_number/list_contact.html'
    paginate_by = 10

    def get_queryset(self):
        print(self.request.user)
        return Contact.objects.filter(owner=self.request.user)



class ContactDetail(DetailView):
    """
    show details of contact on login account
    """
    model = Contact
    context_object_name = 'contact'
    template_name = 'phone_number/detail_contact.html'

class CreateContact(CreateView):
    """
    add new contact on login account
    """
    model = Contact
    fields = ['contact_image', 'contact_name', 'name_contact', 'phone_number', 'email']
    template_name = 'phone_number/create_contact.html'
    success_url = '/phone_number/list-contact/'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.instance.phone_number is None:
            pass
