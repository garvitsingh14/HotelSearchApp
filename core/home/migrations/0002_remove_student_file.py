# Generated by Django 4.2 on 2023-06-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
    ]
