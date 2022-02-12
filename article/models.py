from django.db import models
from current_date import current_date


def directory_name_article(instance, filename, just_date=False):
    year, month, day = current_date()
    if just_date:
        return f'article/{year}/{month}/{day}/'

    # def returner():
    #     try:
    #         flag = instance.lesson.name
    #         flag = 'handout'
    #     except (AttributeError, Exception):
    #         flag = 'lesson'
    #     if filename is not None:
    #         if flag == 'lesson':
    #             return '%s/%s/%s/%s/%s/%s/%s/%s' % (
    #                 'lesson', instance.title, year, month, day, instance.university_name, instance.name, filename)
    #         else:
    #             return '%s/%s/%s/%s/%s/%s/%s/%s' % (
    #                 'handout', instance.title, year, month, day, instance.university_name, instance.name, filename)
    #     else:
    #         if flag == 'lesson':
    #             return '%s/%s/%s/%s/%s/%s/%s' % (
    #                 'lesson', instance.title, year, month, day, instance.university_name, instance.name)
    #         else:
    #             return '%s/%s/%s/%s/%s/%s/%s' % (
    #                 'handout', instance.title, year, month, day, instance.university_name, instance.name)
    return '%s/%s/%s/%s/%s' % ('article', year, month, day, filename)


class ArticleManager(models.Manager):
    def is_confirmed(self):
        return self.filter(is_confirmed=True)

    def not_confirmed(self):
        return self.filter(is_confirmed=False)


class Article(models.Model):
    name = models.CharField(max_length=50, blank=False, default='article')
    title = models.CharField(max_length=255, blank=False)
    subject = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=True, default='admin')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=False)
    is_confirmed = models.BooleanField(default=False, blank=True)
    file = models.FileField(upload_to=directory_name_article, blank=True)

    def __str__(self):
        return f'{self.title} {self.subject}'


    @classmethod
    def confirmed(cls):
        return cls.objects.filter(is_confirmed=True)

    @classmethod
    def not_confirmed(cls):
        return cls.objects.filter(is_confirmed=False)

    objects = ArticleManager()
