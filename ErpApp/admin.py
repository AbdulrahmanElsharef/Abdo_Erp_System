from django.contrib import admin
from .models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display=['name','price_sales','active','status']
    list_display_links=['price_sales','name']
    list_editable=['active','status']
    list_filter=['category','active','status','colors']
    search_fields=['name','details','slug']

admin.site.site_header='ERP_Admin'
admin.site.site_title='ERP_Admin'

admin.site.register(Item,ItemAdmin)
admin.site.register(Category)