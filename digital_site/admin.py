from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Digital)
class AllDigitals(admin.ModelAdmin):
    # list_display = ('id', 'title', 'price', 'get_image')
    list_display = ('id', 'title', 'price')
    list_display_links = ('title',)
    list_filter = ('title', 'price')
    search_fields = ('title__name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="60", height="50" ')

    get_image.short_description = "Images"
    # readonly_fields = ('poster',)


admin.site.register(Product_Name)
admin.site.register(Product_Brend_Model)
admin.site.register(Product_Brend_Name)
admin.site.register(Product_Specifications_Processor)
admin.site.register(Product_Specifications_RAM)
admin.site.register(CarShorts)
admin.site.register(Product_Specifications_Screen)


# @admin.register(Reviews)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'parent', 'car')

# Register your models here.
