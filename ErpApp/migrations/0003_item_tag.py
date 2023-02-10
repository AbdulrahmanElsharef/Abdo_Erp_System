# Generated by Django 3.2 on 2023-02-10 13:02

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('ErpApp', '0002_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]