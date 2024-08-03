from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=300, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.IntegerField()
    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

class Post(models.Model):

    STATUS_CHOICES =(('draft','پیشنویس') ,('published','منشترشده'))

    title = models.CharField(max_length=50 , verbose_name= ('عنوان'))
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE ,blank =True , related_name='author')
    published = models.DateField(auto_now_add=True , blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published',
                              verbose_name='وضعیت انتشار')
    slug = models.SlugField(max_length=50, unique=True)
    thumbnail = models.ImageField(upload_to = 'image/',null=True,)
    category = models.ManyToManyField(Category, related_name='category')

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    get_category.short_description = 'دسته بندی'
