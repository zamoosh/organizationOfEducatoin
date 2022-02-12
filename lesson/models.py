from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from user.models import Student
from jalali_date import datetime2jalali
from current_date import current_date


def directory_name(instance=None, filename=None, just_date=False):
    year, month, day = current_date()
    if just_date:
        return f'lesson/{year}/{month}/{day}/'

    if isinstance(instance, Lesson):
        return '%s/%s/%s/%s/%s' % ('lesson', year, month, day, filename)
    elif isinstance(instance, Handout):
        return '%s/%s/%s/%s/%s' % ('handout', year, month, day, filename)


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    university_name = models.CharField(max_length=70)
    student = models.ManyToManyField(Student, blank=True)
    student_list = models.JSONField(null=True, blank=True)
    grades_list = models.JSONField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=directory_name, blank=True)

    def __str__(self):
        return f'{self.name} {self.title}'

    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.delete(self.image.name)
        super().delete()

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)

    def datetime_to_jalali_update(self):
        return datetime2jalali(self.update)


class Exam(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'exam: {self.title}'

    def delete(self, using=None, keep_parents=False):
        super().delete()

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)


class Handout(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=255, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=True, upload_to=directory_name)

    def __str__(self):
        return f'{self.lesson} {self.title}'

    def delete(self, using=None, keep_parents=False):
        if self.file:
            self.file.delete(self.file.name)
        super().delete()

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)

    def datetime_to_jalali_update(self):
        return datetime2jalali(self.update)


class Notifications(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=255, blank=True, default='admin')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'notification {self.title}'

    def delete(self, using=None, keep_parents=False):
        super().delete()

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)

    def datetime_to_jalali_update(self):
        return datetime2jalali(self.update)


@receiver(signal=pre_delete)
def lesson_delete(**kwargs):
    ins = kwargs['instance']
    if isinstance(ins, Lesson):
        if ins.image:
            ins.image.delete(False)
    elif isinstance(ins, Handout):
        ins.lesson.image.delete(False)
