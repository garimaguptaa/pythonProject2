# Generated by Django 4.1.5 on 2023-01-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
