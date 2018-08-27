from django.contrib import admin

# Register your models here.
from .models import RegistuKursu
class RegistuKursuAdmin(admin.ModelAdmin):
    model = RegistuKursu
    list_display = ('first_name', 'last_name', 'birthday', 'place', 'phonenumber', 'sexo', 'cursu')
    search_fields = ('first_name', 'last_name', 'place', 'phonenumber')


admin.site.register(RegistuKursu, RegistuKursuAdmin)
