# Generated by Django 2.0.2 on 2020-08-13 15:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200706_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 15, 59, 46, 998283, tzinfo=utc), verbose_name='Fecha de Publicación'),
        ),
    ]
