# Generated by Django 2.2.2 on 2019-12-01 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0033_auto_20191201_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_host_documento_fonte',
            name='Titolo_documento_fonte',
        ),
        migrations.RemoveField(
            model_name='model_titolo_documento_fonte',
            name='Autore_documento_fonte',
        ),
        migrations.RemoveField(
            model_name='model_titolo_documento_fonte',
            name='Definizione',
        ),
        migrations.RemoveField(
            model_name='model_titolo_documento_fonte',
            name='Host_documento_fonte',
        ),
        migrations.RemoveField(
            model_name='model_titolo_documento_fonte',
            name='Url_documento_fonte',
        ),
        migrations.RemoveField(
            model_name='model_url_documento_fonte',
            name='Titolo_documento_fonte',
        ),
        migrations.DeleteModel(
            name='model_Autore_documento_fonte',
        ),
        migrations.DeleteModel(
            name='model_Host_documento_fonte',
        ),
        migrations.DeleteModel(
            name='model_Titolo_documento_fonte',
        ),
        migrations.DeleteModel(
            name='model_Url_documento_fonte',
        ),
    ]