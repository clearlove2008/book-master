# Generated by Django 2.0.1 on 2020-02-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_messageboard_look_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageboard',
            name='feebback_num',
            field=models.IntegerField(default=1, verbose_name='回复数'),
        ),
    ]
