# Generated by Django 2.1.5 on 2019-01-18 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistLinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=30)),
                ('venue', models.CharField(max_length=30)),
                ('concert_date', models.DateTimeField(verbose_name='date of concert')),
            ],
        ),
    ]
