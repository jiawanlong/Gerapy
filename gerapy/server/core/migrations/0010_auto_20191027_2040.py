# Generated by Django 2.2.4 on 2019-10-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180711_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
