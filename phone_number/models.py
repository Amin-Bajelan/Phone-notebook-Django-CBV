from django.db import models
from accounts.models import User

# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_image = models.ImageField(upload_to='images/', blank=True,null=True)
    name_contact = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_updated = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"owner: {self.owner}, name_contact: {self.name_contact}"
