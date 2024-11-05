from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return f'{self.id}) {self.name}'


class News(models.Model):
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(verbose_name='изображение', upload_to='news_image/')
    description = models.CharField(max_length=200, verbose_name='описание')
    content = models.TextField(verbose_name='контент')
    date = models.DateTimeField(verbose_name='дата добавление', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='дата изменение', auto_now=True)
    author = models.CharField(max_length=50, verbose_name='автор', null=True, blank=True)
    category = models.ForeignKey('news.Category', on_delete=models.PROTECT, related_name='news', verbose_name='категория')
    views = models.PositiveIntegerField(verbose_name='просмотры', default=0)
    is_published = models.BooleanField(verbose_name='публичность', default=True)
    tags = models.ManyToManyField('news.Tag', related_name='news', verbose_name='теги')
    
    def __str__(self):
        return f'{self.id}) {self.name}'



class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self) -> str:
        return self.name

# Create your models here.
