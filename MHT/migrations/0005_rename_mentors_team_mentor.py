# Generated by Django 4.2.3 on 2023-08-16 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MHT', '0004_membership_teammentor_remove_participant_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='mentors',
            new_name='mentor',
        ),
    ]