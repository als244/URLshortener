# Generated by Django 2.2 on 2019-04-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20190409_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shortened',
            field=models.TextField(default='abcd1234', unique=True),
        ),
    ]