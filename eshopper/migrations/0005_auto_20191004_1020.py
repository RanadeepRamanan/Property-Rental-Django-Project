# Generated by Django 2.2.5 on 2019-10-04 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshopper', '0004_auto_20191004_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_holder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='property holder'),
        ),
    ]