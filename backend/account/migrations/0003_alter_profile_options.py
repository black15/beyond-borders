# Generated by Django 4.1.6 on 2023-02-14 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
    ]