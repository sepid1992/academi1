# Generated by Django 4.2.4 on 2023-08-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_shop_noe'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('msg_subject', models.CharField(max_length=500)),
            ],
        ),
    ]