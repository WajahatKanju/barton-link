# Generated by Django 4.2.1 on 2023-06-18 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0005_rename_tag_type_tag_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='excerpts.tagtype'),
        ),
    ]
