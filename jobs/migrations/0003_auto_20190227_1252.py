# Generated by Django 2.1.5 on 2019-02-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
