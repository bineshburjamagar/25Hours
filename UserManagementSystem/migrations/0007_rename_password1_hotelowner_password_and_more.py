# Generated by Django 4.0.3 on 2022-04-02 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagementSystem', '0006_hotelowner_email_hotelowner_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelowner',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='hotelowner',
            name='password2',
        ),
    ]