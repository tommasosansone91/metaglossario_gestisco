# Generated by Django 2.2.2 on 2019-12-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0032_auto_20191201_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_titolo_documento_fonte',
            name='Autore_documento_fonte',
            field=models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Autore_documento_fonte'),
        ),
        migrations.AlterField(
            model_name='model_titolo_documento_fonte',
            name='Definizione',
            field=models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_titolo_documento_fonte',
            name='Host_documento_fonte',
            field=models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Host_documento_fonte'),
        ),
    ]
