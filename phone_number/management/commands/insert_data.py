from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User,Profile
from phone_number.models import Contact


class Command(BaseCommand):
    help = 'Insert data into database'

    def __init__(self,*args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.faker = Faker()
    def handle(self,*args,**options):
        user = User.objects.create_user(email=self.faker.email(),password=self.faker.password())
        profile = Profile.objects.get(username=user)

