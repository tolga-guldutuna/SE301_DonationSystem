# Generated by Django 2.0 on 2017-12-18 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DonApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donatoruser',
            old_name='profile',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='ngouser',
            old_name='profile',
            new_name='user',
        ),
    ]
