# Generated by Django 2.0.1 on 2018-01-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20180103_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
