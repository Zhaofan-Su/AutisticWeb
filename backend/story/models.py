from django.db import models

# Create your models here.


class Story(models.Model):
    name = models.CharField(max_length=40, verbose_name='姓名', db_column='name')
    age = models.IntegerField(verbose_name='年龄', db_column='age')
    intro = models.TextField(verbose_name='介绍', db_column='intro')

    class Meta:
        db_table = 'story'
        verbose_name_plural = '故事'
        verbose_name = 'story'

    def __str__(self):
        return self.name


class Content(models.Model):
    story = models.ForeignKey(
        Story, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='详情', db_column='content')

    class Meta:
        db_table = 'content'
        verbose_name_plural = '详情'
        verbose_name = 'story'

    def __str__(self):
        return self.story.name + "'s content"
