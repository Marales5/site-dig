from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)


    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})
    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return '{} '' {}'.format(self.title, self.slug)

    class Meta:
        ordering = ['date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return '{} '' {}'.format(self.title, self.slug)

    class Meta:
        ordering = ['title']

    # def get_absolute_url(self):
    #     return reverse('post_detail_url', kwargs={'slug': self.slug})

############## Digital model ###############

class Goods(models.Model):
    title_goods = models.CharField(max_length=50)
    slug_goods = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('single_blog_url', kwargs={'slug_goods': self.slug_goods})

    def __str__(self):
        return '{} '' {}'.format(self.title_goods, self.slug_goods)

    class Meta:
        ordering = ['title_goods']
class GoodsClasses(models.Model):
    title_goods = models.CharField(max_length=50)
    slug_goods = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('single_blog_url', kwargs={'slug_goods': self.slug_goods})

    def __str__(self):
        return '{} '' {}'.format(self.title_goods, self.slug_goods)

    class Meta:
        ordering = ['title_goods']

############# NEW ################

class Product_Name(models.Model):
    """Название продукта"""
    name = models.CharField("Name", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product label"
        verbose_name_plural = "Products label"
class Product_Brend_Name(models.Model):
    """Марка"""
    name = models.CharField("Фирма", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Произовдители"
class Product_Brend_Model(models.Model):
    """Модель"""
    name = models.CharField("Модель", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
class Product_Specifications_Processor(models.Model):
    """Характеристики процесор """

    processor = models.CharField("количество ядер", max_length=100)


    def __str__(self):
        return self.processor

    class Meta:
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"

class Product_Specifications_Screen(models.Model):
    """Характеристики экрана """

    screen = models.CharField("диагональ экрана", max_length=100)


    def __str__(self):
        return self.screen

    class Meta:
        verbose_name = "экран"
        verbose_name_plural = "экраны"

class Product_Specifications_RAM(models.Model):
    """Характеристики RAM """

    ram = models.CharField("объем RAM", max_length=100)


    def __str__(self):
        return self.ram

    class Meta:
        verbose_name = "оперативка"
        verbose_name_plural = "оперативка"



class Digital(models.Model):
    """Устройство"""
    name = models.ManyToManyField(Product_Name, max_length=100)
    title = models.ForeignKey(Product_Brend_Name, verbose_name="Phones Title", null=True, on_delete=models.CASCADE)

    model_digit = models.ManyToManyField(Product_Brend_Model,  max_length=100)
    processor = models.ManyToManyField(Product_Specifications_Processor,  max_length=100)
    screen = models.ManyToManyField(Product_Specifications_Screen,  max_length=100)
    ram = models.ManyToManyField(Product_Specifications_RAM, max_length=100)
    poster = models.ImageField("Фото", null=True, default=None, upload_to="movies/")
    price = models.PositiveIntegerField("Цена", default=0, help_text="указыжите сумму")
    slug = models.SlugField("Url", max_length=150, blank=True, unique=False)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title.name

    def get_absolute_url(self):
        return reverse("digital_detail_url", kwargs={"slug": self.slug})


    # def get_review(self):
    #     return self.reviews_set.filter(parent__isnull=True)


    class Meta:
        verbose_name = "Digital"
        verbose_name_plural = "Digitals"

class CarShorts(models.Model):
    image = models.ImageField("Pictures", null=True, default=None, upload_to="movie_shots/")
    digital = models.ForeignKey(Digital, verbose_name="Car", on_delete=models.CASCADE)

    def __str__(self):
        return self.car.title.name
    class Meta:
        verbose_name = "Short"
        verbose_name_plural = "Shorts"
class CarShorts2(models.Model):
    image = models.ImageField("Pictures", null=True, default=None, upload_to="movie_shots/")
    digital = models.ForeignKey(Digital, verbose_name="Car", on_delete=models.CASCADE)

    def __str__(self):
        return self.car.title.name
    class Meta:
        verbose_name = "Short"
        verbose_name_plural = "Shorts"
