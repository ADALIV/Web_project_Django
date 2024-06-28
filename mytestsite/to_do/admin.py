from django.contrib import admin
from .models import WhatToDo
from .models import do_type

# Register your models here.

admin.site.register(WhatToDo)
admin.site.register(do_type)