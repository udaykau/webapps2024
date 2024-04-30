# Generated by Django 5.0.4 on 2024-04-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0007_alter_points_points_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_your_username', models.CharField(max_length=50)),
                ('enter_destination_username', models.CharField(max_length=50)),
                ('enter_points_to_transfer', models.FloatField()),
                ('transfer_status', models.CharField(choices=[('Pending', 'Pending'), ('approved', 'approved'), ('Rejected', 'Rejected')], default='Pending', max_length=12)),
            ],
        ),
    ]
