# Generated by Django 2.1.5 on 2019-02-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
