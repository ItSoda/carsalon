from django.contrib import admin
from .models import Car, Image


admin.site.register(Image)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id","name", "age", "mileage", "price")
    filter_horizontal = ["photos"]
