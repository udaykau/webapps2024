# Generated by Django 5.0.4 on 2024-04-23 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0009_pointsrequest_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointsrequest',
            name='active',
        ),
    ]
