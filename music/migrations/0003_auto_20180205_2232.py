# Generated by Django 2.0.2 on 2018-02-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180204_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='genre',
        ),
        migrations.AddField(
            model_name='event',
            name='event_artist',
            field=models.CharField(default='Unknown', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateField(verbose_name=['%d-%m-%Y']),
        ),
    ]