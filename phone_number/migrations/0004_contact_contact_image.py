# Generated by Django 5.2.3 on 2025-07-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_number', '0003_alter_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
