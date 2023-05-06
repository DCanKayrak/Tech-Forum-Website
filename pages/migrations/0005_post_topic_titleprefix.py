# Generated by Django 4.2 on 2023-05-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_topic_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlePrefix', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='titlePrefix',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
