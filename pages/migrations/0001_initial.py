# Generated by Django 4.2 on 2023-05-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('answers', models.IntegerField()),
                ('LastUpdate', models.DateField()),
                ('LastMessage', models.CharField(max_length=50)),
            ],
        ),
    ]