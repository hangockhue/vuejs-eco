from django.contrib import admin
from .models import Category, Product, Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__all___')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product)