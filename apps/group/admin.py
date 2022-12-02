from django.contrib import admin

from apps.group.models import EventModel, BikeGroupsModel


@admin.register(EventModel)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_route', 'end_route', 'start_date', 'end_date']


admin.site.register(BikeGroupsModel)
