from django.contrib import admin
from .models import Link, Clicked

# Register your models here.
admin.site.register(Link)
admin.site.register(Clicked)