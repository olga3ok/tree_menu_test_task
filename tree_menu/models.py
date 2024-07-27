from django.db import models
from django.urls import reverse


class Menu(models.Model):

    name = models.CharField('Название меню', max_length=100, blank=False, null=False, unique=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    name = models.CharField('Пункты меню', max_length=150)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children',
    )
    path = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['menu', 'path']
        verbose_name = 'Пункты меню'
        verbose_name_plural = 'Пункты меню'

    def get_path(self):
        if self.parent:
            path = f'{self.parent.path} > {self.name}'
        else:
            path = f'{self.name}'
        return path

    def save(self, *args, **kwargs):
        self.path = self.get_path()
        if self.parent:
            self.menu = self.parent.menu
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', kwargs={'item_id': self.id})
