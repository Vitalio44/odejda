from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Goods(models.Model):
    goods_category = models.ForeignKey(Category, default=1)
    img_url = models.URLField(verbose_name="Ссылка на изображение")
    price = models.CharField(max_length=20, db_index=True, verbose_name="Цена")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ["-goods_category"]

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.img_url

