# Generated by Django 4.1.5 on 2023-01-19 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listings_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bid',
        ),
    ]