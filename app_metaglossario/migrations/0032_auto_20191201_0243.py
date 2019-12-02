# Generated by Django 2.2.2 on 2019-12-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0031_auto_20191201_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_Url_documento_fonte',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Url_documento_fonte', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['Url_documento_fonte', 'ID'],
            },
        ),
        migrations.AlterField(
            model_name='model_titolo_documento_fonte',
            name='Url_documento_fonte',
            field=models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Url_documento_fonte'),
        ),
        migrations.AddField(
            model_name='model_url_documento_fonte',
            name='Titolo_documento_fonte',
            field=models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Titolo_documento_fonte'),
        ),
        migrations.CreateModel(
            name='model_Host_documento_fonte',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Host_documento_fonte', models.TextField(blank=True, null=True)),
                ('Titolo_documento_fonte', models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Titolo_documento_fonte')),
            ],
            options={
                'ordering': ['Host_documento_fonte', 'ID'],
            },
        ),
        migrations.CreateModel(
            name='model_Autore_documento_fonte',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Autore_documento_fonte', models.TextField(blank=True, null=True)),
                ('Titolo_documento_fonte', models.ManyToManyField(blank=True, null=True, to='app_metaglossario.model_Titolo_documento_fonte')),
            ],
            options={
                'ordering': ['Autore_documento_fonte', 'ID'],
            },
        ),
    ]
