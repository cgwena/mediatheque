# Generated by Django 5.0.1 on 2024-02-09 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('loans', '0003_rename_emprunt_loan'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='LibraryUser',
        ),
    ]
