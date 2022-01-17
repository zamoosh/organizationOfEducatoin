from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User


class StudentManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('فیلد ایمیل اجباریست')
        if not username:
            raise ValueError('فیلید شماره دانشجویی اجباریست')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            **extra_fields
        )
        user.is_master = True
        user.is_student = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser):
    username = models.IntegerField(unique=True)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    field = models.CharField(max_length=255, blank=True)
    university = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(upload_to="%Y/%m/%d", blank=True)
    is_master = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
    ]
    objects = StudentManager()

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_master
