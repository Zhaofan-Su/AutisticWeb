# Generated by Django 2.2 on 2019-04-10 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20190408_2213'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='content',
            table='story_content',
        ),
    ]