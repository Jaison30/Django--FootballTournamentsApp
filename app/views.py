# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from random import randint
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta

from .models import *

# Create your views here.


def MatchShedule(date, teams):

    matches = Match()

    matches.date = date
    matches.team_1 = teams[0]
    matches.team_2 = teams[1]
    matches.save()

    return date

@receiver(post_save, sender=Team)
def Creatematches(sender, **kwargs):
    teams = Team.objects.all()
    matches = Match.objects.all()

    if Team.objects.count() >= 6 and matches.count() == 0:
        MatchShedule(datetime.now(), teams[0:2])
        MatchShedule(datetime.now() + timedelta(days=1), teams[2:4])
        MatchShedule(datetime.now() + timedelta(days=2), teams[4::])



class Index(RedirectView):
    url = '/home'



class Home(TemplateView):
    #login_url = '/login/'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        #user = User.objects.get(pk=self.kwargs.get('pk'))
        teams = Team.objects.all()
        matches = Match.objects.all()
        ctx['matches'] = matches
        ctx['teams'] = teams
        ctx['title'] = 'TournamentApp'
        ctx['heading'] = 'TEAMS'
        ctx['rand'] = randint(100, 999)
        
        return ctx


class TeamDetails(TemplateView):
    #login_url = '/login/'
    template_name = 'team-details.html'

    def get_context_data(self, **kwargs):
        ctx = super(TeamDetails, self).get_context_data(**kwargs)

        team = Team.objects.get(pk=self.kwargs.get('pk'))
        ctx['teams'] = []

        managers = Manager.objects.get(team_name=team).name
        coach = Coach.objects.get(team_name=team).name
        members = TeamMember.objects.filter(team_name=team)


        ctx['title'] = 'TournamentApp'
        ctx['rand'] = randint(100, 999)
        ctx['teams'].append({'id':team.id,'team_name':team.name,'image':team.image,'coach':coach,'members':members,'managers':managers,'goal_scored':team.goal_scored,'no_of_matches':team.no_of_matches,'no_of_matches_win':team.no_of_matches_win})
        
        print 'ctx', ctx
        
        return ctx



class AddTeam(View):

    #login_url = '/login/'

    def get(self, request, *args, **kwargs):
        #user = User.objects.get(pk=self.kwargs.get('pk'))
        #print 'user', user

        team = Team.objects.all()
        
        ctx = {}
        ctx['title'] = 'TournamentApp'
        ctx['heading'] = 'TEAM REGISTERATION'

        ctx['registration_complete'] = False
        if team.count() >= 6:
            ctx['registration_complete'] = True
        ctx['rand'] = randint(100, 999)
        return render(request, 'create-team.html', ctx)

    def post(self, request, *args, **kwargs):

        #user = User.objects.get(pk=self.kwargs.get('pk'))

        redirect_url = reverse('add-team')
        success_url = reverse('registration-success')

        team_name = self.request.POST.get('team_name')
        manager_name = self.request.POST.get('manager')
        coach_name = self.request.POST.get('coach')
        team_logo = self.request.FILES.get('team_logo')
        player_1 = self.request.POST.get('player_1')
        player_2 = self.request.POST.get('player_2')
        player_3 = self.request.POST.get('player_3')
        player_4 = self.request.POST.get('player_4')
        player_5 = self.request.POST.get('player_5')
        player_6 = self.request.POST.get('player_6')
        player_7 = self.request.POST.get('player_7')
        player_8 = self.request.POST.get('player_8')
        player_9 = self.request.POST.get('player_9')
        player_10 = self.request.POST.get('player_10')
        player_11 = self.request.POST.get('player_11')

        print 'team_logo', team_logo

        team = Team()
        teamMember = TeamMember()
        coach = Coach()
        manager = Manager()

        if Team.objects.filter(name=team_name).exists():
                messages.error(self.request, "The Team is already Exist")
                return HttpResponseRedirect(redirect_url)

        team.name = team_name
        team.image = team_logo
        team.save()

        manager.name = manager_name
        manager.team_name = team
        manager.save()

        coach.name = coach_name
        coach.team_name = team
        coach.save()

        teamMember1 = TeamMember(name=player_1, team_name=team)
        teamMember1.save()
        teamMember2 = TeamMember(name=player_2, team_name=team)
        teamMember2.save()
        teamMember3 = TeamMember(name=player_3, team_name=team)
        teamMember3.save()
        teamMember4 = TeamMember(name=player_4, team_name=team)
        teamMember4.save()
        teamMember5 = TeamMember(name=player_5, team_name=team)
        teamMember5.save()
        teamMember6 = TeamMember(name=player_6, team_name=team)
        teamMember6.save()
        teamMember7 = TeamMember(name=player_7, team_name=team)
        teamMember7.save()
        teamMember8 = TeamMember(name=player_8, team_name=team)
        teamMember8.save()
        teamMember9 = TeamMember(name=player_9, team_name=team)
        teamMember9.save()
        teamMember10 = TeamMember(name=player_10, team_name=team)
        teamMember10.save()
        teamMember11 = TeamMember(name=player_11, team_name=team)
        teamMember11.save()

        return HttpResponseRedirect(success_url)


class TeamRegistrationSuccess(TemplateView):
    #login_url = '/login/'
    template_name = 'registration-success.html'

    def get_context_data(self, **kwargs):
        ctx = super(TeamRegistrationSuccess, self).get_context_data(**kwargs)
        ctx['title'] = 'TournamentApp'
        ctx['heading'] = 'TournamentApp'
        ctx['username'] = 'Admin'
        ctx['rand'] = randint(100, 999)
        
        return ctx
