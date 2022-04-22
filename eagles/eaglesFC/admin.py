from django.contrib import admin
from .models import Teams, BookingAndPurchasesHistory, TeamFormationModel, Newsletter

admin.site.register(Teams)
admin.site.register(BookingAndPurchasesHistory)
admin.site.register(TeamFormationModel)
admin.site.register(Newsletter)