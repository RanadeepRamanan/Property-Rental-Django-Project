# Generated by Django 2.2.5 on 2019-09-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]