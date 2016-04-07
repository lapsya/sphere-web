from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Vendor)
admin.site.register(ShippingMethod)
admin.site.register(Order)
admin.site.register(Cart)

#@admin.register(ShopUser)
class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name',
                        'email', 'is_active', 'is_staff', 'is_superuser', 'groups',
                        'user_permissions', 'birth_date', 'address', 'bill', 'discount',
                        'cart', 'laid_off', 'orders'),
        }),
    )
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(UserAdmin, self).get_fieldsets(request, obj)

admin.site.register(ShopUser, MyUserAdmin)
