from django.contrib import admin
from .models import League
from cup.models import Cup

class LeagueAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "domestic_cup":
            kwargs["queryset"] = Cup.objects.filter(status="Domestic Cup")
        if db_field.name == "league_cup":
            kwargs["queryset"] = Cup.objects.filter(status="League Cup")
        if db_field.name == "international_cup":
            kwargs["queryset"] = Cup.objects.filter(status="International Cup")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(League, LeagueAdmin)
