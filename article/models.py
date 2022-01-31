from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False)
    subject = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=True, default='admin')
    create = models.DateTimeField(auto_now_add=True, blank=False)
    update = models.DateTimeField(auto_now=True, blank=False)
    description = models.TextField(blank=False)
    is_confirmed = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f'{self.title} {self.subject}'
