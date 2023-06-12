# Generated by Django 4.2.1 on 2023-06-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0003_remove_excerptsimilarity_spacy_similarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='excerpt',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='excerpt',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
