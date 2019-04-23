from django.db import models


# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=40, verbose_name='标题', db_column='name')
    intro = models.TextField(verbose_name='简介', db_column='intro')

    class Meta:
        db_table = 'information'
        verbose_name_plural = '相关信息'
        verbose_name = 'information'

    def __str__(self):
        return self.name


class Content(models.Model):
    information = models.ForeignKey(
        Information, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='内容', db_column='content')

    class Meta:
        db_table = 'informationContent'
        verbose_name = 'content'
        verbose_name_plural = '段落'

    def __str__(self):
        return self.information.name + "'s content"


class SubTitle(models.Model):
    information = models.ForeignKey(
        Information, related_name='sub_titles', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=50, verbose_name='子标题', db_column='title')

    class Meta:
        db_table = 'subtitle'
        verbose_name_plural = '子标题'
        verbose_name = 'subtitle'

    def __str__(self):
        return self.information.name + "'s 子标题 " + self.title


class SubContent(models.Model):
    sub_title = models.ForeignKey(
        SubTitle, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='内容', db_column='content')

    class Meta:
        db_table = 'sub_content'
        verbose_name = 'sub_content'
        verbose_name_plural = '子段落'

    def __str__(self):
        return self.sub_title.title + "'s content"


class ListTitle(models.Model):
    information = models.ForeignKey(
        Information, related_name='list_titles', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=50, verbose_name='列表标题', db_column='title')

    class Meta:
        db_table = 'list_title'
        verbose_name = 'list_title'
        verbose_name_plural = '列表标题'

    def __str__(self):
        return self.information.name + "'s " + self.title


class ListContent(models.Model):
    list_title = models.ForeignKey(
        ListTitle, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='内容', db_column='content')

    class Meta:
        db_table = 'list_content'
        verbose_name = 'list_content'
        verbose_name_plural = '列表段落'

    def __str__(self):
        return self.list_title.title + "'s content"
