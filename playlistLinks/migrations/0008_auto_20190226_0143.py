# Generated by Django 2.1.5 on 2019-02-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistLinks', '0007_update_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
