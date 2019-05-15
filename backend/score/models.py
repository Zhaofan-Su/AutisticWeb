from django.db import models
from rest_framework import serializers


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=40,
                             verbose_name="标题",
                             db_column="title")
    proper = models.CharField(max_length=200,
                              verbose_name="与年龄相当",
                              db_column="proper")
    mild = models.CharField(max_length=200,
                            verbose_name="轻度异常",
                            db_column="mild")
    moderate = models.CharField(max_length=200,
                                verbose_name="中度异常",
                                db_column="moderate")
    badly = models.CharField(max_length=200,
                             verbose_name="严重异常",
                             db_column="badly")

    class Meta:
        db_table = 'question'
        verbose_name_plural = '测试题'
        verbose_name = 'question'

    def __str__(self):
        return self.title


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("title", "proper", "mild", "moderate", "badly")
