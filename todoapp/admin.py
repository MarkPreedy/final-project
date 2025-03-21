from django.contrib import admin
from .models import Category, Task, SubTask

# Register models in the admin panel
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
