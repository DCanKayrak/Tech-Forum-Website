# Generated by Django 4.2 on 2023-05-06 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_carouselimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarouselImages',
            new_name='CarouselImage',
        ),
    ]
