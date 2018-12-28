from django.contrib import admin

from core.models import Car, User


class CarAdmin(admin.ModelAdmin):
    search_fields = ('title', 'brand', 'mileage')
    list_display = ('title', 'brand', 'mileage')


admin.site.register(Car, CarAdmin)
admin.site.register(User)
