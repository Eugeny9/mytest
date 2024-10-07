from django.contrib import admin

from myappp.models import product

class myconfigprod(admin.ModelAdmin):
    list_display = ['name','height', 'width', 'cost']

admin.site.register(product,myconfigprod)

# Register your models here.
