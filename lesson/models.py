from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from jalali_date import datetime2jalali
from user.models import Student
from current_date import current_date


def age_validator(age):
    if not (18 <= age <= 90):
        raise ValueError(f"age should be in range 18 to 75")


def directory_name(instance=None, filename=None, just_date=False):
    year, month, day = current_date()
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
        print('hello world!')
        pass

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
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=255, blank=True, default='admin')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'notification {self.title}'

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


@receiver(post_save)
def printer(**kwargs):
    print('hello world!')
