# Generated by Django 2.2 on 2019-04-08 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20190408_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='story.Story'),
        ),
    ]
