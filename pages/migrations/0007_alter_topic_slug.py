# Generated by Django 4.2 on 2023-05-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_topic_slug_alter_topic_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]