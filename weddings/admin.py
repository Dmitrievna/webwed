from django.contrib import admin
from weddings.models import Wedding
from weddings.models import Task
from weddings.models import Category
from weddings.models import Supplier
from weddings.models import Table
from weddings.models import Guest
from weddings.models import Location
from weddings.models import Budget

# Register your models here.
admin.site.register(Wedding)
admin.site.register(Task)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(Guest)
admin.site.register(Location)
admin.site.register(Budget)
