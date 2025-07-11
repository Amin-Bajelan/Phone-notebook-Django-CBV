from django.urls import path
from . import views


urlpatterns = [
    # get list of contact with ability filter
    path('list_contact/', views.ContactPhoneNumberList.as_view(), name='list_contact'),
    # get detail of one contact, create add update get
    path('list_contact/<int:pk>/', views.ContactPhoneNumberDetail.as_view(), name='contact_detail'),
    #create super user
    path('create_superuser/', views.SuperUserCreateView.as_view(), name='create_superuser'),
]