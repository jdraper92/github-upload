# Generated by Django 2.1.5 on 2019-01-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistLinks', '0005_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='city',
            field=models.CharField(default='Chicago', max_length=30),
        ),
    ]
