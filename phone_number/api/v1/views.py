from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from phone_number.api.v1.serializers import ContactSerializer

from phone_number.models import Contact
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import SuperUserSerializer



class ContactPhoneNumberList(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['owner__User', 'created_at']
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactPhoneNumberDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

class SuperUserCreateView(CreateAPIView):
    serializer_class = SuperUserSerializer
    permission_classes = [IsAdminUser]