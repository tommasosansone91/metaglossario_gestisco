# Generated by Django 2.2.2 on 2019-10-14 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0004_auto_20191007_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossary_entry',
            name='Commento_entry',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='glossary_entry',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 10, 14)),
        ),
    ]