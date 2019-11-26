# Generated by Django 2.2.2 on 2019-11-24 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0016_auto_20191119_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='is_Acronimo_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Admin_approval_switch_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Ambito_riferimento_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Autore_definizione_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Autore_documento_fonte_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Commento_entry_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Data_inserimento_entry_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Host_documento_fonte_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Id_statico_entry_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Lemma_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Posizione_definizione_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Url_definizione_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='is_Url_documento_fonte_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(blank=True, max_length=25, null=True)),
                ('ID_oggetto', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(blank=True, max_length=25, null=True)),
                ('Oggetto', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['ID', 'Oggetto'],
            },
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 24)),
        ),
        migrations.AlterField(
            model_name='displaying_terminology',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 24)),
        ),
        migrations.AlterField(
            model_name='glossary_entry',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 24)),
        ),
        migrations.AlterField(
            model_name='glossary_file',
            name='Data_inserimento_glossary',
            field=models.DateField(default=datetime.date(2019, 11, 24)),
        ),
        migrations.AlterField(
            model_name='prepared_terminology',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 24)),
        ),
    ]