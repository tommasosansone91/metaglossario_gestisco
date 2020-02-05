# Generated by Django 2.2.2 on 2020-02-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0047_delete_displaying_terminology'),
    ]

    operations = [
        migrations.DeleteModel(
            name='model_is_Acronimo_of',
        ),
        migrations.DeleteModel(
            name='model_is_Admin_approval_switch_of',
        ),
        migrations.DeleteModel(
            name='model_is_Ambito_riferimento_of',
        ),
        migrations.DeleteModel(
            name='model_is_Autore_definizione_of',
        ),
        migrations.DeleteModel(
            name='model_is_Autore_documento_fonte_of',
        ),
        migrations.DeleteModel(
            name='model_is_Commento_entry_of',
        ),
        migrations.DeleteModel(
            name='model_is_Data_inserimento_entry_of',
        ),
        migrations.DeleteModel(
            name='model_is_Host_documento_fonte_of',
        ),
        migrations.DeleteModel(
            name='model_is_Id_statico_entry_of',
        ),
        migrations.DeleteModel(
            name='model_is_Lemma_of',
        ),
        migrations.DeleteModel(
            name='model_is_Posizione_definizione_of',
        ),
        migrations.DeleteModel(
            name='model_is_Titolo_documento_fonte_of',
        ),
        migrations.DeleteModel(
            name='model_is_Url_definizione_of',
        ),
        migrations.DeleteModel(
            name='model_is_Url_documento_fonte_of',
        ),
        migrations.DeleteModel(
            name='model_Things',
        ),
        migrations.AlterModelOptions(
            name='acquired_terminology',
            options={'ordering': ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Data_inserimento_entry', 'Id_statico_entry']},
        ),
        migrations.AlterModelOptions(
            name='glossary_entry',
            options={'ordering': ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Data_inserimento_entry', 'Id_statico_entry']},
        ),
        migrations.AlterModelOptions(
            name='prepared_terminology',
            options={'ordering': ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Data_inserimento_entry', 'Id_statico_entry']},
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Acronimo',
            new_name='Acronimo_ch',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Ambito_riferimento',
            new_name='Ambito_riferimento_ch',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Lemma',
            new_name='Ambito_riferimento_it',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Autore_definizione',
            new_name='Autore_definizione_ch',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Autore_documento_fonte',
            new_name='Autore_definizione_it',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Definizione',
            new_name='Autore_documento_fonte_ch',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Host_documento_fonte',
            new_name='Autore_documento_fonte_it',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Posizione_definizione',
            new_name='Definizione_ch',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Titolo_documento_fonte',
            new_name='Definizione_it',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Url_definizione',
            new_name='Url_definizione_ch',
        ),
        migrations.RenameField(
            model_name='acquired_terminology',
            old_name='Url_documento_fonte',
            new_name='Url_definizione_it',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Acronimo',
            new_name='Acronimo_ch',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Ambito_riferimento',
            new_name='Ambito_riferimento_ch',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Lemma',
            new_name='Ambito_riferimento_it',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Autore_definizione',
            new_name='Autore_definizione_ch',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Autore_documento_fonte',
            new_name='Autore_definizione_it',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Definizione',
            new_name='Autore_documento_fonte_ch',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Host_documento_fonte',
            new_name='Autore_documento_fonte_it',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Posizione_definizione',
            new_name='Definizione_ch',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Titolo_documento_fonte',
            new_name='Definizione_it',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Url_definizione',
            new_name='Url_definizione_ch',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Url_documento_fonte',
            new_name='Url_definizione_it',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Acronimo',
            new_name='Acronimo_ch',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Ambito_riferimento',
            new_name='Ambito_riferimento_ch',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Lemma',
            new_name='Ambito_riferimento_it',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Autore_definizione',
            new_name='Autore_definizione_ch',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Autore_documento_fonte',
            new_name='Autore_definizione_it',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Definizione',
            new_name='Autore_documento_fonte_ch',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Host_documento_fonte',
            new_name='Autore_documento_fonte_it',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Posizione_definizione',
            new_name='Definizione_ch',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Titolo_documento_fonte',
            new_name='Definizione_it',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Url_definizione',
            new_name='Url_definizione_ch',
        ),
        migrations.RenameField(
            model_name='prepared_terminology',
            old_name='Url_documento_fonte',
            new_name='Url_definizione_it',
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Acronimo_it',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Host_documento_fonte_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Host_documento_fonte_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Lemma_ch',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Lemma_it',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Posizione_definizione_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Posizione_definizione_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Titolo_documento_fonte_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Titolo_documento_fonte_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Url_documento_fonte_ch',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='acquired_terminology',
            name='Url_documento_fonte_it',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Acronimo_it',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Host_documento_fonte_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Host_documento_fonte_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Lemma_ch',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Lemma_it',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Posizione_definizione_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Posizione_definizione_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Titolo_documento_fonte_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Titolo_documento_fonte_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Url_documento_fonte_ch',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='glossary_entry',
            name='Url_documento_fonte_it',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Acronimo_it',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Host_documento_fonte_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Host_documento_fonte_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Lemma_ch',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Lemma_it',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Posizione_definizione_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Posizione_definizione_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Titolo_documento_fonte_ch',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Titolo_documento_fonte_it',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Url_documento_fonte_ch',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='prepared_terminology',
            name='Url_documento_fonte_it',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]