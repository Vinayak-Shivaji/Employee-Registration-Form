# Generated by Django 4.1.7 on 2023-07-08 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='empcode',
            new_name='emp_code',
        ),
    ]
