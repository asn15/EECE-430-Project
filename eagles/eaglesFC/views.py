from multiprocessing import context
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Newsletter, Teams, BookingAndPurchasesHistory, TeamFormationModel, Newsletter
from django.shortcuts import render
from django.urls import reverse

def Home(response):
  last_five_games = Teams.objects.all().order_by('-id')[:5]
  template = loader.get_template('Home.html')
  if response.method == 'POST':
    Name = response.POST.get('name')
    Email = response.POST.get('email')
    NewsletterForm = Newsletter(name=Name, email=Email)
    NewsletterForm.save()
    # context = {
    #   "empty": "",
    # }
    # return HttpResponseRedirect(reverse('Home'))
  context = {
    "last_five_games": last_five_games,
  }
  return HttpResponse(template.render(context, response))

def bookingAndPurchasesHistoryFunc(response):
  BookingAndPurchasesHistoryContext = BookingAndPurchasesHistory.objects.all().order_by('-id')
  template = loader.get_template('BookingandPurchaseshistory.html')
  context = {
    "BookingAndPurchasesHistory": BookingAndPurchasesHistoryContext,
  }
  if response.method == 'POST':
    Name = response.POST.get('name')
    Email = response.POST.get('email')
    NewsletterForm = Newsletter(name=Name, email=Email)
    NewsletterForm.save()
  return HttpResponse(template.render(context, response))


def TeamFormation(response):
  template = loader.get_template('teamformation.html')
  GK_SP, DF_SP_L, DF_SP_LM, DF_SP_RM, DF_SP_R, MF_SP_L, MF_SP_LM, MF_SP_RM, MF_SP_R, FW_SP_LW, FW_SP_RW, GK_NS, DF_NS_1, DF_NS_2, MF_NS_1, MF_NS_2, FW_NS_LW, FW_NS_RW = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
  if (TeamFormationModel.objects.get()):
    TeamFormationTemp = TeamFormationModel.objects.get()
    GK_SP = TeamFormationTemp.GK_SP
    DF_SP_L = TeamFormationTemp.DF_SP_L
    DF_SP_LM = TeamFormationTemp.DF_SP_LM
    DF_SP_RM = TeamFormationTemp.DF_SP_RM
    DF_SP_R = TeamFormationTemp.DF_SP_R
    MF_SP_L = TeamFormationTemp.MF_SP_L
    MF_SP_LM = TeamFormationTemp.MF_SP_LM
    MF_SP_RM = TeamFormationTemp.MF_SP_RM
    MF_SP_R = TeamFormationTemp.MF_SP_R
    FW_SP_LW = TeamFormationTemp.FW_SP_LW
    FW_SP_RW = TeamFormationTemp.FW_SP_RW  
    GK_NS = TeamFormationTemp.GK_NS
    DF_NS_1 = TeamFormationTemp.DF_NS_1
    DF_NS_2 = TeamFormationTemp.DF_NS_2
    MF_NS_1 = TeamFormationTemp.MF_NS_1
    MF_NS_2 = TeamFormationTemp.MF_NS_2
    FW_NS_LW = TeamFormationTemp.FW_NS_LW
    FW_NS_RW = TeamFormationTemp.FW_NS_RW
    if response.POST.get('FormSP'):
      GK_SP = response.POST.get('GK_SP')
      DF_SP_L = response.POST.get('DF_SP_L')
      DF_SP_LM = response.POST.get('DF_SP_LM')
      DF_SP_RM = response.POST.get('DF_SP_RM')
      DF_SP_R = response.POST.get('DF_SP_R')
      MF_SP_L = response.POST.get('MF_SP_L')
      MF_SP_LM = response.POST.get('MF_SP_LM')
      MF_SP_RM = response.POST.get('MF_SP_RM')
      MF_SP_R = response.POST.get('MF_SP_R')
      FW_SP_LW = response.POST.get('FW_SP_LW')
      FW_SP_RW = response.POST.get('FW_SP_RW')
      if (TeamFormationModel.objects.get()):
        TeamFormationTemp = TeamFormationModel.objects.get()
        TeamFormationTemp.GK_SP = GK_SP
        TeamFormationTemp.DF_SP_L = DF_SP_L
        TeamFormationTemp.DF_SP_LM = DF_SP_LM
        TeamFormationTemp.DF_SP_RM = DF_SP_RM
        TeamFormationTemp.DF_SP_R = DF_SP_R
        TeamFormationTemp.MF_SP_L = MF_SP_L
        TeamFormationTemp.MF_SP_LM = MF_SP_LM
        TeamFormationTemp.MF_SP_RM = MF_SP_RM
        TeamFormationTemp.MF_SP_R = MF_SP_R
        TeamFormationTemp.FW_SP_LW = FW_SP_LW
        TeamFormationTemp.FW_SP_RW = FW_SP_RW
        TeamFormationTemp.save()
      else:
        TeamFormationTemp = TeamFormationModel(GK_SP=GK_SP, DF_SP_L=DF_SP_L, DF_SP_LM=DF_SP_LM, DF_SP_RM=DF_SP_RM, DF_SP_R=DF_SP_R, MF_SP_L=MF_SP_L, MF_SP_LM=MF_SP_LM, MF_SP_RM=MF_SP_RM, MF_SP_R=MF_SP_R, FW_SP_LW=FW_SP_LW, FW_SP_RW=FW_SP_RW, GK_NS=GK_NS, DF_NS_1=DF_NS_1, DF_NS_2=DF_NS_2, MF_NS_1=MF_NS_1, MF_NS_2=MF_NS_2, FW_NS_LW=FW_NS_LW, FW_NS_RW=FW_NS_RW)
        TeamFormationTemp.save()
    if response.POST.get('FormNS'):
      GK_NS = response.POST.get('GK_NS')
      DF_NS_1 = response.POST.get('DF_NS_1')
      DF_NS_2 = response.POST.get('DF_NS_2')
      MF_NS_1 = response.POST.get('MF_NS_1')
      MF_NS_2 = response.POST.get('MF_NS_2')
      FW_NS_LW = response.POST.get('FW_NS_LW')
      FW_NS_RW = response.POST.get('FW_NS_RW')
      if (TeamFormationModel.objects.get()):
        TeamFormationTemp = TeamFormationModel.objects.get()
        TeamFormationTemp.GK_NS = GK_NS
        TeamFormationTemp.DF_NS_1 = DF_NS_1
        TeamFormationTemp.DF_NS_2 = DF_NS_2
        TeamFormationTemp.MF_NS_1 = MF_NS_1
        TeamFormationTemp.MF_NS_2 = MF_NS_2
        TeamFormationTemp.FW_NS_LW = FW_NS_LW
        TeamFormationTemp.FW_NS_RW = FW_NS_RW
        TeamFormationTemp.save()
      else:
        TeamFormationTemp = TeamFormationModel(GK_SP=GK_SP, DF_SP_L=DF_SP_L, DF_SP_LM=DF_SP_LM, DF_SP_RM=DF_SP_RM, DF_SP_R=DF_SP_R, MF_SP_L=MF_SP_L, MF_SP_LM=MF_SP_LM, MF_SP_RM=MF_SP_RM, MF_SP_R=MF_SP_R, FW_SP_LW=FW_SP_LW, FW_SP_RW=FW_SP_RW, GK_NS=GK_NS, DF_NS_1=DF_NS_1, DF_NS_2=DF_NS_2, MF_NS_1=MF_NS_1, MF_NS_2=MF_NS_2, FW_NS_LW=FW_NS_LW, FW_NS_RW=FW_NS_RW)
        TeamFormationTemp.save()

  if response.POST.get('hidden'):
    Name = response.POST.get('name')
    Email = response.POST.get('email')
    NewsletterForm = Newsletter(name=Name, email=Email)
    NewsletterForm.save()

  context = {
    "GK_SP": GK_SP,
    "DF_SP_L": DF_SP_L,
    "DF_SP_LM": DF_SP_LM,
    "DF_SP_RM": DF_SP_RM,
    "DF_SP_R": DF_SP_R,
    "MF_SP_L": MF_SP_L,
    "MF_SP_LM": MF_SP_LM,
    "MF_SP_RM": MF_SP_RM,
    "MF_SP_R": MF_SP_R,
    "FW_SP_LW": FW_SP_LW,
    "FW_SP_RW": FW_SP_RW,
    "GK_NS": GK_NS,
    "DF_NS_1": DF_NS_1,
    "DF_NS_2": DF_NS_2,
    "MF_NS_1": MF_NS_1,
    "MF_NS_2": MF_NS_2,
    "FW_NS_LW": FW_NS_LW,
    "FW_NS_RW": FW_NS_RW,
  }
  return render(response, 'TeamFormation.html', context)


def AdminPage(request):
  myteams = Teams.objects.all().values()
  mynewsletters = Newsletter.objects.all().values()
  mybookingandpurchaseshistory = BookingAndPurchasesHistory.objects.all().values()
  myteamformation = TeamFormationModel.objects.all().values()
  template = loader.get_template('adminpage.html')
  context = {
    'myteams': myteams,
    'mynewsletters': mynewsletters,
    'mybookingandpurchaseshistory': mybookingandpurchaseshistory,
    'myteamformation': myteamformation,
  }
  return HttpResponse(template.render(context, request))


# Upcoming Matches

def addupcomingmatches(request):
  template = loader.get_template('adminaddupcomingmatches.html')
  return HttpResponse(template.render({}, request))
  
def addrecordupcomingmatches(request):
  time = request.POST['time']
  homeTeam = request.POST['homeTeam']
  awayTeam = request.POST['awayTeam']
  team = Teams(time=time, homeTeam=homeTeam, awayTeam=awayTeam)
  team.save()
  return HttpResponseRedirect(reverse('AdminPage'))

def deleteupcomingmatches(request, id):
  team = Teams.objects.get(id=id)
  team.delete()
  return HttpResponseRedirect(reverse('AdminPage'))
  
def updateupcomingmatches(request, id):
  myteam = Teams.objects.get(id=id)
  template = loader.get_template('adminupdateupcomingmatches.html')
  context = {
    'myteam': myteam,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecordupcomingmatches(request, id):
  time = request.POST.get('time')
  homeTeam = request.POST.get('homeTeam')
  awayTeam = request.POST.get('awayTeam')
  team = Teams.objects.get(id=id)
  team.time = time
  team.homeTeam = homeTeam
  team.awayTeam = awayTeam
  team.save()
  return HttpResponseRedirect(reverse('AdminPage'))

# Newsletters

def addnewsletter(request):
  template = loader.get_template('adminaddnewsletter.html')
  return HttpResponse(template.render({}, request))
  
def addrecordnewsletter(request):
  name = request.POST['name']
  email = request.POST['email']
  newsletter = Newsletter(name=name, email=email)
  newsletter.save()
  return HttpResponseRedirect(reverse('AdminPage'))

def deletenewsletter(request, id):
  newsletter = Newsletter.objects.get(id=id)
  newsletter.delete()
  return HttpResponseRedirect(reverse('AdminPage'))
  
def updatenewsletter(request, id):
  mynewsletter = Newsletter.objects.get(id=id)
  template = loader.get_template('adminupdatenewsletter.html')
  context = {
    'mynewsletter': mynewsletter,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecordnewsletter(request, id):
  name = request.POST.get('name')
  email = request.POST.get('email')
  newsletter = Newsletter.objects.get(id=id)
  newsletter.name = name
  newsletter.email = email
  newsletter.save()
  return HttpResponseRedirect(reverse('AdminPage'))


# Booking and Purchases History

def addbookingandpurchaseshistory(request):
  template = loader.get_template('adminaddbookingandpurchaseshistory.html')
  return HttpResponse(template.render({}, request))
  
def addrecordbookingandpurchaseshistory(request):
  time = request.POST['time']
  description = request.POST['description']
  history = BookingAndPurchasesHistory(time=time, description=description)
  history.save()
  return HttpResponseRedirect(reverse('AdminPage'))

def deletebookingandpurchaseshistory(request, id):
  history = BookingAndPurchasesHistory.objects.get(id=id)
  history.delete()
  return HttpResponseRedirect(reverse('AdminPage'))
  
def updatebookingandpurchaseshistory(request, id):
  myhistory = BookingAndPurchasesHistory.objects.get(id=id)
  template = loader.get_template('adminupdatebookingandpurchaseshistory.html')
  context = {
    'myhistory': myhistory,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecordbookingandpurchaseshistory(request, id):
  time = request.POST.get('time')
  description = request.POST.get('description')
  myhistory = BookingAndPurchasesHistory.objects.get(id=id)
  myhistory.time = time
  myhistory.description = description
  myhistory.save()
  return HttpResponseRedirect(reverse('AdminPage'))


# Team Formation
  
def updateteamformation(request, id):
  myteamformation = TeamFormationModel.objects.get(id=id)
  template = loader.get_template('adminupdateteamformation.html')
  context = {
    'myteamformation': myteamformation,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecordteamformation(request, id):
  GK_SP = request.POST.get('GK_SP')
  DF_SP_L = request.POST.get('DF_SP_L')
  DF_SP_LM = request.POST.get('DF_SP_LM')
  DF_SP_RM = request.POST.get('DF_SP_RM')
  DF_SP_R = request.POST.get('DF_SP_R')
  MF_SP_L = request.POST.get('MF_SP_L')
  MF_SP_LM = request.POST.get('MF_SP_LM')
  MF_SP_RM = request.POST.get('MF_SP_RM')
  MF_SP_R = request.POST.get('MF_SP_R')
  FW_SP_LW = request.POST.get('FW_SP_LW')
  FW_SP_RW = request.POST.get('FW_SP_RW')
  GK_NS = request.POST.get('GK_NS')
  DF_NS_1 = request.POST.get('DF_NS_1')
  DF_NS_2 = request.POST.get('DF_NS_2')
  MF_NS_1 = request.POST.get('MF_NS_1')
  MF_NS_2 = request.POST.get('MF_NS_2')
  FW_NS_LW = request.POST.get('FW_NS_LW')
  FW_NS_RW = request.POST.get('FW_NS_RW')
  
  teamformation = TeamFormationModel.objects.get(id=id)
  teamformation.GK_SP = GK_SP
  teamformation.DF_SP_L = DF_SP_L
  teamformation.DF_SP_LM = DF_SP_LM
  teamformation.DF_SP_RM = DF_SP_RM
  teamformation.DF_SP_R = DF_SP_R
  teamformation.MF_SP_L = MF_SP_L
  teamformation.MF_SP_LM = MF_SP_LM
  teamformation.MF_SP_RM = MF_SP_RM
  teamformation.MF_SP_R = MF_SP_R
  teamformation.FW_SP_LW = FW_SP_LW
  teamformation.FW_SP_RW = FW_SP_RW
  teamformation.GK_NS = GK_NS
  teamformation.DF_NS_1 = DF_NS_1
  teamformation.DF_NS_2 = DF_NS_2
  teamformation.MF_NS_1 = MF_NS_1
  teamformation.MF_NS_2 = MF_NS_2
  teamformation.FW_NS_LW = FW_NS_LW
  teamformation.FW_NS_RW = FW_NS_RW

  teamformation.save()
  return HttpResponseRedirect(reverse('AdminPage'))
