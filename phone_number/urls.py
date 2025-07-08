from django.urls import path
from . import views


urlpatterns = [
    path('list-contact/',views.ListContact.as_view(),name='list-contact'),
    path('contact/detail/<int:pk>',views.ContactDetail.as_view(),name='detail-contact'),
    path('add_contact/',views.CreateContact.as_view(),name='add-contact'),
    path('show_profile/',views.ShowProfile.as_view(),name='profile'),
    path('delete_contact/<int:pk>',views.DeleteContact.as_view(),name='delete-contact'),

]