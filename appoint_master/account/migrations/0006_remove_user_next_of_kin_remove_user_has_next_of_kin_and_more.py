# Generated by Django 5.0.1 on 2025-04-04 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_prescription_prescribed_for_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='next_of_kin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_next_of_kin',
        ),
        migrations.DeleteModel(
            name='NextOfKin',
        ),
    ]
