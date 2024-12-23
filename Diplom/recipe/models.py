from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование блюда')
    describe = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Состав')
    steps = models.TextField(verbose_name='Способ приготовления')
    image = models.ImageField('foto', upload_to='recipe_img', blank=True)
    image1 = models.URLField('Дополнительное изображение', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
# Create your models here.
