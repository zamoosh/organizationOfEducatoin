from django.db import models
from jalali_date import datetime2jalali


class Feedback(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True, default='notification')
    author = models.CharField(max_length=255, blank=True, default='admin')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'notification {self.title}'

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)

    def datetime_to_jalali_update(self):
        return datetime2jalali(self.update)
