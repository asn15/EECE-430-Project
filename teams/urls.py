from django.urls import path
from . import views
from django.conf.urls import url
from .views import Home, TeamsListView, ScoresListView, PlayerDetailsView, TeamDetailsView, AddTeamView, \
    AddPlayerView, DeleteEvent, errorbooking, Consultations, DeleteConsultations, Contact, News

urlpatterns = [
    path('', views.Home, name='Home'),
    path('home', views.Home, name='Home'),
    path('bookingandpurchaseshistory', views.bookingAndPurchasesHistoryFunc, name='BookingAndPurchasesHistory'),
    path('teamformation', views.TeamFormation, name='TeamFormation'),

    path('adminpage', views.AdminPage, name='AdminPage'),

    path('login', views.Login, name='Login'),
    path('register', views.Register, name='Register'),

    path('adminpage/addupcomingmatches/', views.addupcomingmatches, name='add'),
    path('adminpage/addupcomingmatches/addrecordupcomingmatches/', views.addrecordupcomingmatches, name='addrecord'),
    path('adminpage/deleteupcomingmatches/<int:id>', views.deleteupcomingmatches, name='delete'),
    path('adminpage/updateupcomingmatches/<int:id>', views.updateupcomingmatches, name='update'),
    path('adminpage/updateupcomingmatches/updaterecordupcomingmatches/<int:id>', views.updaterecordupcomingmatches, name='updaterecord'),
    
    path('adminpage/addnewsletter/', views.addnewsletter, name='add'),
    path('adminpage/addnewsletter/addrecordnewsletter/', views.addrecordnewsletter, name='addrecord'),
    path('adminpage/deletenewsletter/<int:id>', views.deletenewsletter, name='delete'),
    path('adminpage/updatenewsletter/<int:id>', views.updatenewsletter, name='update'),
    path('adminpage/updatenewsletter/updaterecordnewsletter/<int:id>', views.updaterecordnewsletter, name='updaterecord'),

    path('adminpage/addbookingandpurchaseshistory/', views.addbookingandpurchaseshistory, name='add'),
    path('adminpage/addbookingandpurchaseshistory/addrecordbookingandpurchaseshistory/', views.addrecordbookingandpurchaseshistory, name='addrecord'),
    path('adminpage/deletebookingandpurchaseshistory/<int:id>', views.deletebookingandpurchaseshistory, name='delete'),
    path('adminpage/updatebookingandpurchaseshistory/<int:id>', views.updatebookingandpurchaseshistory, name='update'),
    path('adminpage/updatebookingandpurchaseshistory/updaterecordbookingandpurchaseshistory/<int:id>', views.updaterecordbookingandpurchaseshistory, name='updaterecord'),

    path('adminpage/updateteamformation/<int:id>', views.updateteamformation, name='update'),
    path('adminpage/updateteamformation/updaterecordteamformation/<int:id>', views.updaterecordteamformation, name='updaterecord'),   


    url(r'^teams/$', TeamsListView.as_view(), name="teams-list-view"),
    url(r'^scores/$', ScoresListView.as_view(), name="scores-list-view"),

    url(r'^player/(?P<slug>[-\w\x20]+)/$', PlayerDetailsView.as_view(), name="player-details-view"),
    url(r'^team/(?P<slug>[-\w\x20]+)/$', TeamDetailsView.as_view(), name="team-details-view"),

    url(r'^add_team/$', AddTeamView.as_view(), name="add-team-view"),
    url(r'^add_player/$', AddPlayerView.as_view(), name="add-player-view"),
    url(r'^delete_matches/$', DeleteEvent, name="delete-matches-view"),
    url(r'^consultation/$', Consultations.as_view(), name="consultation"),
    url(r'^delete_consultation/$', DeleteConsultations, name="delete-consultation-view"),
    url(r'^contact/$', Contact, name="contact-view"),
    url(r'^latest_news/$', News, name="news-view"),

]