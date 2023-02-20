from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.title}"


class Products(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(to='my_market.Category', null=False, blank=False, verbose_name="Категория", related_name="product", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    price = models.DecimalField(null=False, blank=False, verbose_name="Цена", max_digits=12, decimal_places=2)
    picture = models.URLField(max_length=1000, blank=False, null=False, verbose_name="URL картинка")

    def __str__(self):
        return f"{self.title} - {self.created_at}"