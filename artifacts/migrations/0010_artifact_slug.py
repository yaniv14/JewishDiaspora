# Generated by Django 2.0 on 2017-12-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0009_auto_20171222_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, verbose_name='Slug'),
        ),
    ]
