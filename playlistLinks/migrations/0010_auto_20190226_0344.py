# Generated by Django 2.1.5 on 2019-02-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistLinks', '0009_auto_20190226_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='concert',
            name='band',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='concert',
            name='city',
            field=models.CharField(default='Chicago', max_length=100),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default='Chicago', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
