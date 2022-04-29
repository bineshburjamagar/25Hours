# Generated by Django 4.0.3 on 2022-04-20 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomManagementSystem', '0017_reserveddetails_payement_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserveddetails',
            name='payement_completed',
        ),
        migrations.CreateModel(
            name='bookedDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(max_length=30)),
                ('check_out', models.DateField(max_length=30)),
                ('total_price', models.FloatField()),
                ('payement_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('rooms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomManagementSystem.rooms')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]