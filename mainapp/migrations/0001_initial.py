# Generated by Django 4.0 on 2021-12-16 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('Discription', models.CharField(max_length=200)),
                ('release_year', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField()),
                ('fulltext', models.PositiveIntegerField()),
                ('lastupdate', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loandate', models.DateTimeField(blank=True)),
                ('returndate', models.DateTimeField(blank=True)),
                ('lastupdate', models.DateTimeField(blank=True)),
                ('mediaid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.media')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200)),
                ('postalcode', models.CharField(max_length=200)),
                ('phone', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=200)),
                ('lastupdate', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
