# Generated by Django 4.0.1 on 2022-01-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='student',
            name='field',
            field=models.CharField(blank=True, max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(blank=True, max_length=255, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(blank=True, max_length=255, verbose_name='دانشگاه'),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.IntegerField(unique=True, verbose_name='شماره دانشجویی'),
        ),
    ]