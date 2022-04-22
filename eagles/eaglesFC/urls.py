from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('home', views.Home, name='Home'),
    path('bookingandpurchaseshistory', views.bookingAndPurchasesHistoryFunc, name='BookingAndPurchasesHistory'),
    path('teamformation', views.TeamFormation, name='TeamFormation'),

    path('adminpage', views.AdminPage, name='AdminPage'),

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
]