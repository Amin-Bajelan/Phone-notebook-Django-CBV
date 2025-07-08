from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from phone_number.models import Contact
from accounts.models import Profile


# Create your views here.


class ListContact(ListView):
    """
    show list of all  contacts on login account
    """
    model = Contact
    context_object_name = 'contacts'
    template_name = 'phone_number/list_contact.html'
    paginate_by = 5

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

    def get_context_data(self, **kwargs):
        Contact.objects.get(id=self.kwargs['pk'])


class CreateContact(CreateView):
    """
    add new contact on login account
    """
    model = Contact
    fields = ['contact_image', 'name_contact', 'phone_number', 'email']
    template_name = 'phone_number/create_contact.html'
    success_url = '/phone_number/list-contact/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return redirect('/phone_number/list-contact/')


class ShowProfile(TemplateView):
    """
    show profile on login account
    """
    model = Profile
    template_name = "phone_number/profile.html"
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(username=self.request.user)


class DeleteContact(DeleteView):
    model = Contact
    template_name = "phone_number/delete_contact.html"
    success_url = '/phone_number/list-contact/'


class DetailContact(DetailView):
    model = Contact
    template_name = 'phone_number/detail_contact.html'
