from django.db import models

# Create your models here.


class Story(BaseModel):
    name = models.CharField(max_length=30, verbose_name='姓名', db_column='name')
    age = models.IntegerField(verbose_name='年龄', db_column='age')
    intro = models.CharField(
        max_length=400, verbose_name='介绍', db_column='intro')

    class Meta:
        db_table = 'story'
        verbose_name_plural = '故事'
        verbose_name = '故事'
