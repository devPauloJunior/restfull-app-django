# Generated by Django 4.2.1 on 2023-06-22 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='doctors_first_name',
            new_name='doctor_first_name',
        ),
        migrations.RenameField(
            model_name='doctors',
            old_name='doctors_id',
            new_name='doctor_id',
        ),
        migrations.RenameField(
            model_name='doctors',
            old_name='doctors_last_name',
            new_name='doctor_last_name',
        ),
        migrations.RenameField(
            model_name='doctors',
            old_name='doctors_type_blood',
            new_name='doctor_type_blood',
        ),
    ]
