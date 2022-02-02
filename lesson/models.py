from django.db import models
from jalali_date import datetime2jalali
import datetime
import jdatetime

from user.models import Student


def age_validator(age):
    if not (18 <= age <= 90):
        raise ValueError(f"age should be in range 18 to 75")


def lesson_directory_name(instance, filename):
    current_date = datetime.date.today()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    j = jdatetime.date.fromgregorian(day=day, month=month, year=year, locale='fa_IR')
    day = j.day
    month = j.month
    year = j.year
    return '%s/%s/%s/%s/%s/%s' % ('lesson', instance.name, year, month, day, filename)


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    university_name = models.CharField(max_length=70)
    student = models.ManyToManyField(Student, blank=True)
    student_list = models.JSONField(null=True, blank=True)
    grades_list = models.JSONField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='%y/%m/%d/lesson/', blank=True)

    def __str__(self):
        return f'{self.name} {self.title}'

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

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)


def handout_directory_name(instance, filename):
    current_date = datetime.date.today()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    j = jdatetime.date.fromgregorian(day=day, month=month, year=year, locale='fa_IR')
    day = j.day
    month = j.month
    year = j.year
    return '%s/%s/%s/%s/%s/%s' % ('handout', instance.lesson.name, year, month, day, filename)


class Handout(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=255, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=True, upload_to=handout_directory_name)

    def __str__(self):
        return f'{self.lesson} {self.title}'

    def datetime_to_jalali_create(self):
        return datetime2jalali(self.create)

    def datetime_to_jalali_update(self):
        return datetime2jalali(self.update)


class Notifications(models.Model):
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
