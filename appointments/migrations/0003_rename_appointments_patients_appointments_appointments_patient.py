# Generated by Django 4.2.1 on 2023-06-30 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointments_appointments_patients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='appointments_patients',
            new_name='appointments_patient',
        ),
    ]