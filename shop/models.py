from djongo import models
from django import forms


class ProductExtraField(models.Model):
    name = models.CharField(max_length=255,verbose_name="Наименование")
    value = models.TextField(verbose_name="Значение")

    def __str__(self):
        return f"{self.name} - {self.value}"

    class Meta:
        abstract = True


class ProductExtraFieldForm(forms.ModelForm):
    class Meta:
        model = ProductExtraField
        fields = (
            'name', 'value'
        )


class ProductCategory(models.Model):
    """
    Категория товара
    """

    name = models.CharField(max_length=100, verbose_name="Наименование",blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ProductTag(models.Model):
    """
    Тэг товара
    """

    name = models.CharField(max_length=100, verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Тэг товар"
        verbose_name_plural="Тэги товаров"


class Product(models.Model):
    """
    Товар
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )
    price = models.FloatField(
        verbose_name="Цена",
        default=0,
        blank=True,
    )
    count = models.IntegerField(
        verbose_name="Количество товара на складе",
        default=0,
        blank=True,
    )
    product_extra_fields = models.ArrayField(
        blank=True,
        model_container=ProductExtraField,
        model_form_class=ProductExtraFieldForm,
    )
    product_category = models.EmbeddedField(
        model_container=ProductCategory,
        verbose_name="Категория товара",
        blank=True,
    )
    product_tags = models.ArrayReferenceField(
        to=ProductTag,
        on_delete=models.CASCADE,
        verbose_name="Тэги",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"



class СustomerContacts(models.Model):
    """
    Контакты пользователя
    """

    phone = models.CharField(max_length=100, verbose_name="Номер телефона",blank=True,)
    email = models.CharField(max_length=100, verbose_name="Электронная почта",blank=True,)



    class Meta:
        abstract = True


class Сustomer(models.Model):
    """
    Покупатель
    """


    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    second_name = models.CharField(max_length=255, verbose_name="Отчество",blank=True,)

    сustomer_contacts = models.EmbeddedField(
        model_container=СustomerContacts, verbose_name="Контакты",blank=True,
    )

    class Meta:
        verbose_name="Покупатель"
        verbose_name_plural="Покупатели"