# Generated by Django 4.0.3 on 2022-04-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomManagementSystem', '0005_alter_rooms_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_number',
            field=models.FloatField(max_length=30, null=True),
        ),
    ]
