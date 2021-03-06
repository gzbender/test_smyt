import inspect

from django.contrib import admin
from django.db.models import Model

from test_smyt.models import generated_models, Category, Product, Phone, Item
# Register your models here.

for name, model in generated_models.models.items():
    admin.site.register(model)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Phone)
admin.site.register(Item)