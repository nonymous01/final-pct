# Generated by Django 5.0.3 on 2024-08-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NUMARTISAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionpack',
            name='photo_pack',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
