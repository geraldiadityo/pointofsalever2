from django.contrib import admin

# Register your models here.
from .models import Item_p

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'stok',
        'created',
    ]

admin.site.register(Item_p,ItemAdmin)
