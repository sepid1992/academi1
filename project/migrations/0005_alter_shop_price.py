# Generated by Django 4.2.4 on 2023-08-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_shop_ax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.IntegerField(),
        ),
    ]