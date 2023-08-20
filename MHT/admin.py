from django.contrib import admin
from .models import participant,team,teamMentor,membership

# Register your models here.
@admin.register(participant)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(team)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(teamMentor)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(membership)
class BookAdmin(admin.ModelAdmin):
    pass