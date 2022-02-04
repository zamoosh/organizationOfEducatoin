from django.db import models
from lesson.models import directory_name


def directory_name_article(instance, filename):
    day, month, year = directory_name(just_date=True)
    if filename is None:
        return '%s/%s/%s/%s/%s/%s/%s' % ('article', instance.subject, instance.title, year, month, day, instance.name)
    return '%s/%s/%s/%s/%s/%s/%s/%s' % (
        'article', instance.subject, instance.title, year, month, day, instance.name, filename)


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
