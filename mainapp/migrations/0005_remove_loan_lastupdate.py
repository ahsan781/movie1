# Generated by Django 4.0 on 2021-12-16 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_media_fulltext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='lastupdate',
        ),
    ]
