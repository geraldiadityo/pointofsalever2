from django.contrib import admin
from .models import Supplier
# Register your models here.
class AdminSupplier(admin.ModelAdmin):
    readonly_fields = [
        'created',
    ]

admin.site.register(Supplier,AdminSupplier)
