from django.db import models


class User(models.Model):
    user_name = models.CharField('Username', max_length=30)
    user_phone = models.CharField('Phone', max_length=30)
    user_email = models.EmailField('email')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
