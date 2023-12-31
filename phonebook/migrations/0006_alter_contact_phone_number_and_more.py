# Generated by Django 4.2.7 on 2023-11-28 23:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0005_contact_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='contact',
            name='room_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
