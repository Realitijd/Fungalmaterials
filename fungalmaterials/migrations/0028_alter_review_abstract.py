# Generated by Django 4.2.16 on 2024-09-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fungalmaterials", "0027_alter_article_abstract"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="abstract",
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
