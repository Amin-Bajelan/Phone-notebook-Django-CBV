from django.urls import path
from . import views


urlpatterns = [
    path('list-contact/',views.ListContact.as_view(),name='list-contact'),
    path('contact/detail/<int:pk>',views.ContactDetail.as_view(),name='detail-contact'),
    path('add_contact/',views.CreateContact.as_view(),name='add-contact'),
    path('show_profile/',views.ShowProfile.as_view(),name='show-profile'),
    path('delete_contact/<int:pk>',views.DeleteContact.as_view(),name='delete-contact'),
    path("update_contact/<int:pk>",views.UpdateContact.as_view(),name='update-contact'),
    path("update_profile/",views.UpdateProfile.as_view(),name='update-profile'),

]