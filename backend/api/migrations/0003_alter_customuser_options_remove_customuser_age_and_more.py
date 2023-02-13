# Generated by Django 4.1.6 on 2023-02-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth_day',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'In Algeria'), (2, 'Out Algeria')], null=True, verbose_name='User Type'),
        ),
    ]
