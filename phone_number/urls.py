from django.urls import path
from . import views


urlpatterns = [
    path('list-contact/',views.ListContact.as_view(),name='list-contact'),
    path('contact/detail/<int:id>',views.ContactDetail.as_view(),name='detail-contact'),
    path('add-contact/',views.CreateContact.as_view(),name='add-contact'),
]