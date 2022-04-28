from django.contrib import admin

# Register your models here.
# to display tables in '/admin' we need to register models here
from teams.models import Team, Player, GameScore, Teams, BookingAndPurchasesHistoryModel, TeamFormationModel, Newsletter, Users

admin.site.register(Team)
admin.site.register(Player)

admin.site.register(Teams)
admin.site.register(BookingAndPurchasesHistoryModel)
admin.site.register(TeamFormationModel)
admin.site.register(Newsletter)

admin.site.register(Users)