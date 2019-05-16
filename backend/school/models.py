from django.db import models
from rest_framework import serializers


# Create your models here.
class School(models.Model):
    province = models.CharField(max_length=40,
                                verbose_name='province',
                                db_column='province')
    city = models.CharField(max_length=40,
                            blank=True,
                            verbose_name='city',
                            db_column='city')
    name = models.CharField(max_length=500,
                            verbose_name='name',
                            db_column='name')

    class Meta:
        db_table = 'school'
        verbose_name = 'school'
        verbose_name_plural = '机构'

    def __str__(self):
        return self.province + self.city + self.name


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('province', 'city', 'name')