# Generated by Django 2.0.1 on 2018-01-02 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180102_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-updated_at']},
        ),
    ]