# Generated by Django 2.2 on 2021-05-06 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_address',
            new_name='email',
        ),
    ]
