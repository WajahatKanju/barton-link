# Generated by Django 4.2.1 on 2023-06-11 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcerptSimilarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbert_similarity', models.FloatField()),
                ('spacy_similarity', models.FloatField()),
                ('excerpt1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excerpt1', to='excerpts.excerpt')),
                ('excerpt2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excerpt2', to='excerpts.excerpt')),
            ],
        ),
    ]
