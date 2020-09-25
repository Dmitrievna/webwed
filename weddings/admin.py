from django.contrib import admin
from weddings.models import Wedding
from weddings.models import Task
from weddings.models import Occupation
from weddings.models import Supplier
from weddings.models import Table
from weddings.models import Guest

# Register your models here.
admin.site.register(Wedding)
admin.site.register(Task)
admin.site.register(Supplier)
admin.site.register(Occupation)
admin.site.register(Table)
admin.site.register(Guest)
