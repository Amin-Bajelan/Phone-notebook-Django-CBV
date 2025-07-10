from django.shortcuts import redirect
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from phone_number.models import Contact
from accounts.models import Profile
from django.utils import timezone


# Create your views here.


class ListContact(ListView,LoginRequiredMixin):
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


class ContactDetail(DetailView,LoginRequiredMixin):
    """
    show details of contact on login account
    """
    model = Contact
    context_object_name = 'contact'
    template_name = 'phone_number/detail_contact.html'


class CreateContact(CreateView,LoginRequiredMixin):
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


class ShowProfile(DetailView,LoginRequiredMixin):
    """
    show profile on login account
    """
    model = Profile
    template_name = "phone_number/profile.html"
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(username=self.request.user)


class DeleteContact(DeleteView,LoginRequiredMixin):
    """
    delete contact on login account
    """
    model = Contact
    template_name = "phone_number/delete_contact.html"
    success_url = '/phone_number/list-contact/'


class UpdateContact(UpdateView,LoginRequiredMixin):
    """
    update contact on login account
    """
    model = Contact
    fields = ['contact_image', 'name_contact', 'phone_number', 'email']
    template_name = 'phone_number/update_contact.html'
    context_object_name = 'contact'
    success_url = '/phone_number/list-contact/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_updated = True
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)


class UpdateProfile(UpdateView,LoginRequiredMixin):
    """
    edit profile on login account
    """
    model = Profile
    fields = ['image', 'first_name', 'last_name', 'description']
    success_url = '/phone_number/list-contact/'
    template_name = 'accounts/profile_form.html'

    def get_object(self):
        return Profile.objects.get(username=self.request.user)

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
