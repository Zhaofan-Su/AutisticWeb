# Generated by Django 2.2 on 2019-05-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190515_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(db_column='city', default=None, max_length=40, verbose_name='city'),
        ),
    ]
