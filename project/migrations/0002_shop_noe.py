# Generated by Django 4.2.4 on 2023-08-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='noe',
            field=models.IntegerField(default=1),
        ),
    ]