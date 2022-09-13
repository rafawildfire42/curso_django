# Generated by Django 4.1.1 on 2022-09-13 15:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
        migrations.AddField(
            model_name='post',
            name='alterado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 13, 15, 56, 32, 361336, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunhos', max_length=10),
        ),
    ]
