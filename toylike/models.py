from django.db import models


# Create your models here.


class Blessing(models.Model):
    sender = models.CharField(max_length=50, null=False, blank=False, verbose_name='sender')
    message = models.CharField(max_length=200, null=False, blank=False, verbose_name='message')

    class Meta:
        verbose_name = 'Blessing'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sender
