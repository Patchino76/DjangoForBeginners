# Generated by Django 4.1.3 on 2023-05-25 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_gender',
            new_name='gender',
        ),
    ]
