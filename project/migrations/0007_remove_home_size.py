# Generated by Django 4.2.4 on 2023-09-02 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_home'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='size',
        ),
    ]