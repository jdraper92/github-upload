# Generated by Django 2.1.5 on 2019-02-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistLinks', '0008_auto_20190226_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='band',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.CharField(max_length=60),
        ),
    ]
