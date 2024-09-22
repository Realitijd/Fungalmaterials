# Generated by Django 4.2.16 on 2024-09-22 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fungalmaterials', '0024_remove_article_authors_remove_review_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='author',
            name='sequence',
        ),
        migrations.CreateModel(
            name='ReviewAuthorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.CharField(blank=True, choices=[('first', 'first'), ('additional', 'additional')], max_length=20)),
                ('affiliation', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fungalmaterials.author')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fungalmaterials.review')),
            ],
            options={
                'unique_together': {('author', 'review', 'sequence')},
            },
        ),
        migrations.CreateModel(
            name='ArticleAuthorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.CharField(blank=True, choices=[('first', 'first'), ('additional', 'additional')], max_length=20)),
                ('affiliation', models.CharField(blank=True, max_length=100)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fungalmaterials.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fungalmaterials.author')),
            ],
            options={
                'unique_together': {('author', 'article', 'sequence')},
            },
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(through='fungalmaterials.ArticleAuthorship', to='fungalmaterials.author', verbose_name='Author(s)'),
        ),
        migrations.AddField(
            model_name='review',
            name='authors',
            field=models.ManyToManyField(through='fungalmaterials.ReviewAuthorship', to='fungalmaterials.author', verbose_name='Author(s)'),
        ),
    ]
