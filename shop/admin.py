from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Vendor)
admin.site.register(ShippingMethod)
admin.site.register(ShopUser)
