from django.contrib import admin
from calculation.models import User, Spent, Building


admin.site.register(User)

#Building Register
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['title', 'area']

#Spent Register
@admin.register(Spent)
class SpentAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'price']
    