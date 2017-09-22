from django.contrib import admin
from .models import Category, Goods


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "id"]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Category


class GoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "goods_category", "price"]
    list_filter = ["goods_category", "price"]

    class Meta:
        model = Goods

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
