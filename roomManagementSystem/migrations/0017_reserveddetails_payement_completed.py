# Generated by Django 4.0.3 on 2022-04-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomManagementSystem', '0016_reserveddetails_delete_bookingdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserveddetails',
            name='payement_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
