# Generated by Django 4.2 on 2023-04-27 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_remove_user_email_arrivals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrivals',
            old_name='user_id',
            new_name='username',
        ),
    ]
