from django.contrib.auth.models import AbstractUser
from django.db import models


class Cities(models.Model):
    city = models.CharField('Город', max_length=50, unique=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Categories(models.Model):
    category = models.CharField('Категории', max_length=50, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Qualifications(models.Model):
    qualification = models.CharField('Квалификация', max_length=50, unique=True)

    def __str__(self):
        return self.qualification

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'


class Users(AbstractUser):
    patronymic = models.CharField('Отчество', max_length=50, null=True)
    birth = models.DateField('Дата рождения', auto_now_add=True)
    photo = models.ImageField('Фото пользователя', upload_to='', null=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)
    street = models.CharField('Улица', max_length=50, null=True)
    home = models.CharField('Дом', max_length=50, null=True)
    apartment = models.CharField('Квартира', max_length=50, null=True)
    phone = models.CharField('Номер телефона', max_length=50, null=True)


class Feedbacks(models.Model):
    feedback = models.TextField('Отзывы')
    date = models.DateField('Дата', auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Services(models.Model):
    service = models.CharField('Сервис', max_length=50)
    price = models.IntegerField('Цена')
    desc = models.CharField('Описание', max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сервис'


class Staff(models.Model):
    name = models.CharField('Имя', max_length=50)
    portfolio = models.ImageField('Портфолио', upload_to='')
    qualification = models.ForeignKey(Qualifications, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
