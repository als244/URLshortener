# Generated by Django 2.2 on 2019-04-10 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20190410_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clicked',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shortener.Link'),
        ),
    ]
