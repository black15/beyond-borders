# Generated by Django 4.1.6 on 2023-02-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_birth_day_alter_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Phone Number'),
        ),
    ]