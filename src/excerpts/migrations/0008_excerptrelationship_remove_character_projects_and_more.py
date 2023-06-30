# Generated by Django 4.2.1 on 2023-06-29 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excerpts', '0007_alter_tag_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcerptRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='character',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='excerpt',
            name='projects',
        ),
        migrations.AlterField(
            model_name='excerpt',
            name='metadata',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='excerptrelationship',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='excerpts.excerpt'),
        ),
        migrations.AddField(
            model_name='excerptrelationship',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='excerpts.excerpt'),
        ),
        migrations.AddField(
            model_name='excerpt',
            name='parents',
            field=models.ManyToManyField(related_name='children', through='excerpts.ExcerptRelationship', to='excerpts.excerpt'),
        ),
    ]