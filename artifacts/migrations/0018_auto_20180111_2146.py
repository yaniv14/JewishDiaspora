# Generated by Django 2.0 on 2018-01-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0017_auto_20180107_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='displayed_at',
        ),
        migrations.AddField(
            model_name='artifact',
            name='displayed_at_en',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Artifact location in museum English'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='displayed_at_he',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Artifact location in museum Hebrew'),
        ),
    ]
