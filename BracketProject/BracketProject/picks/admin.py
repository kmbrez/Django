from django.contrib import admin
from .models import Team, Region


class TeamInline(admin.TabularInline):
    model = Team
    extra = 15


class RegionAdmin(admin.ModelAdmin):
    inlines = [TeamInline]


admin.site.register(Region, RegionAdmin)