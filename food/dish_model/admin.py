from django.contrib import admin

# Register your models here.
from .models import dish,chef,Address
admin.site.register(dish)
admin.site.register(chef)
admin.site.register(Address)
