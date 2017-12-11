import threading
from django.core.mail import send_mail
from snippets.models import Snippet, TShirt, Profile, SocialNetwork, Stock, Message, Clap, Follower, Notification
from snippets.serializers import UserSerializer, SnippetSerializer, TShirtSerializer, ProfileSerializer, SocialNetworkSerializer, StockSerializer, MessageSerializer, ClapSerializer, FollowerSerializer, NotificationSerializer
from rest_framework import generics
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.db.models import Q
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import json

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        # msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        # msg.content_subtype = "html"
        # msg.send()
        send_mail(
        self.subject,
        self.html_content,
        'admin@dirstuff.com',
        [self.recipient_list],
        html_message='<p>' + self.html_content + '</p>' + 
        '<br>Please visit our website at:' +
        '<br>https://www.dirstuff.com' + '<br>' +
        '<br>...Best Regards...<br><strong>!!!Dirstuff Team!!!</strong>'
        )

class NotificationThread(threading.Thread):
    def __init__(self, currentUser, notificationType):
        self.currentUser = currentUser
        self.notificationType = notificationType
        threading.Thread.__init__(self)

    def run (self):
        queryset = Profile.objects.all()
        profiles = queryset.filter(owner=self.currentUser)
        profile = profiles[0]

        followers = Follower.objects.all()
        followers = followers.filter(profile=profile)

        for foll in followers:
            userName = foll.username
            ps = queryset.filter(owner__username=userName)
            profileOwner = ps[0]
            notif = Notification(profile=profileOwner, profileId=profile.id, type=self.notificationType)
            notif.save()
    
def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()

def create_new_notification(currentUser, notificationType):
    NotificationThread(currentUser, notificationType).start()

###################################################

import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@scheduler.scheduled_job("interval", seconds=500, id="test")
def test_job():
    # time.sleep(4)
    print ("I'm a test job!")
    # raise ValueError("Olala!")

@scheduler.scheduled_job("interval", seconds=50, id="rating")
def rating_job():
    print ("................Begin Update ratings...............")

    profiles = Profile.objects.all()
    socialNetworks = SocialNetwork.objects.all()
    snippets = Snippet.objects.all()
    followers = Follower.objects.all()
    claps = Clap.objects.all()

    for profile in profiles:
        socials = socialNetworks.filter(owner=profile.owner)
        snips = snippets.filter(owner=profile.owner)
        folls = followers.filter(profile=profile)
        clps = claps.filter(profile=profile)

        nSocial = socials.count()
        nSnippet = snips.count()
        nFollow = folls.count()
        nClap = clps.count()
        
        rating = 0.1*nSocial + 0.05*nSnippet + 0.03*nFollow + 0.1*nClap
        if rating > 5.0:
            rating = 5.0

        profile.rating = rating
        profile.save()

    print ("................End Update ratings...............")

register_events(scheduler)
scheduler.start()
print ("Scheduler started!")