from django.contrib import admin
from tutorial.quickstart.models import Bill

class BillAdmin(admin.ModelAdmin):
    list_prr_page = 20
    list_display = ("title", "ware", "cose")
    
admin.register(Bill, BillAdmin)
