# Generated by Django 4.2 on 2023-05-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_alter_topic_is_commentable'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category'),
            preserve_default=False,
        ),
    ]