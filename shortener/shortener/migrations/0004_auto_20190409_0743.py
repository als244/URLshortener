# Generated by Django 2.2 on 2019-04-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20190409_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shortened',
            field=models.CharField(default='abcd1234', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]