from django.db import models
from jalali_date import datetime2jalali
import datetime
import jdatetime
from user.models import Student


def age_validator(age):
    if not (18 <= age <= 90):
        raise ValueError(f"age should be in range 18 to 75")


def directory_name(instance=None, filename=None, just_date=False):
    current_date = datetime.date.today()
    year, month, day = current_date.year, current_date.month, current_date.day
    j = jdatetime.date.fromgregorian(day=day, month=month, year=year, locale='fa_IR')
    day, month, year = j.day, j.month, j.year
    if just_date:
        return f'lesson/{year}/{month}/{day}/'

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
    return '%s/%s/%s/%s/%s' % ('lesson', year, month, day, filename)


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
