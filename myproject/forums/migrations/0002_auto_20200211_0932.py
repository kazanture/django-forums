# Generated by Django 3.0.3 on 2020-02-11 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_by',
            new_name='user_created',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='starter',
            new_name='user_created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to='forums.Forum'),
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
