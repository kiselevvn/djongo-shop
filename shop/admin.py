from django.contrib import admin
from .models import Product, ProductTag, Сustomer


admin.site.register([ProductTag,Сustomer])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Товар в админке
    """

    list_display = (
        "name",
        "price",
        "count",
    )

    list_filter = (
        "product_tags",
        "product_category",
    )

@admin.register(Сustomer)
class СustomerAdmin(admin.ModelAdmin):
    """
    Покупатель в админке
    """

    list_display = (
        "last_name",
        "first_name",
        "second_name",
    )