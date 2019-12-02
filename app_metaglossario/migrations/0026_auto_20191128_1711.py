# Generated by Django 2.2.2 on 2019-11-28 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0025_auto_20191128_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_is_acronimo_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_acronimo_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_acronimo_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_acronimo_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_admin_approval_switch_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_admin_approval_switch_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_admin_approval_switch_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_admin_approval_switch_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_ambito_riferimento_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_ambito_riferimento_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_ambito_riferimento_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_ambito_riferimento_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_autore_definizione_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_autore_definizione_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_autore_definizione_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_autore_definizione_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_autore_documento_fonte_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_autore_documento_fonte_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_autore_documento_fonte_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_autore_documento_fonte_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_commento_entry_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_commento_entry_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_commento_entry_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_commento_entry_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_data_inserimento_entry_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_data_inserimento_entry_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_data_inserimento_entry_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_data_inserimento_entry_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_host_documento_fonte_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_host_documento_fonte_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_host_documento_fonte_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_host_documento_fonte_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_id_statico_entry_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_id_statico_entry_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_id_statico_entry_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_id_statico_entry_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_lemma_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_lemma_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_lemma_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_lemma_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_posizione_definizione_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_posizione_definizione_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_posizione_definizione_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_posizione_definizione_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_titolo_documento_fonte_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_titolo_documento_fonte_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_titolo_documento_fonte_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_titolo_documento_fonte_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_url_definizione_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_url_definizione_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_url_definizione_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_url_definizione_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_url_documento_fonte_of',
            name='ID_oggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_url_documento_fonte_of_as_oggetto', to='app_metaglossario.model_Things'),
        ),
        migrations.AlterField(
            model_name='model_is_url_documento_fonte_of',
            name='ID_soggetto',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='model_is_url_documento_fonte_of_as_soggetto', to='app_metaglossario.model_Things'),
        ),
    ]
