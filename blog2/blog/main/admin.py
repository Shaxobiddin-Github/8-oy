from django.contrib import admin

# Register your models here.

from .models import Klass, Mexmonxona, Travel

admin.site.register(Klass)

admin.site.register(Mexmonxona)

admin.site.register(Travel)