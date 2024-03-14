from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Category(models.Model):
    #courses_Category
    #Cái này mặc định sẽ là khóa chính và không tự tạo ra PK
    #name = models.CharField(primary_key=True)

    #NGuoclai
    name = models.CharField(max_length=100,null=False,unique=True)

class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default= None)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Course(ItemBase):

    class Meta:
        unique_together = ('subject', 'category')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Lesson(ItemBase):
    class Meta:
        unique_together =('subject', 'course')
        ordering = ["-id"]
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)




