# Generated by Django 3.0.3 on 2020-02-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0004_auto_20200211_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
