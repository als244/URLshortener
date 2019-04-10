# Generated by Django 2.2 on 2019-04-09 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='link',
            name='shortened',
            field=models.CharField(default='abcd1234', max_length=8, unique=True),
        ),
        migrations.AddField(
            model_name='link',
            name='timeCreated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.TextField(default=''),
        ),
    ]