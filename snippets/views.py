from snippets.models import Snippet, TShirt, Profile, SocialNetwork, Stock, Message, Clap
from snippets.serializers import UserSerializer, SnippetSerializer, TShirtSerializer, ProfileSerializer, SocialNetworkSerializer, StockSerializer, MessageSerializer, ClapSerializer
from rest_framework import generics
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly, IsMySelfOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
# import qrcode
import pyqrcode
import uuid
import urllib
from django.db.models import Q
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from snippets.utils import send_html_mail
import json
from django.contrib.auth import update_session_auth_hash

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SnippetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class UserList(generics.ListAPIView):
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned Users to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/users?username=tony
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMySelfOrReadOnly)

class ProfileList(generics.ListCreateAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    pagination_class = StandardResultsSetPagination

    filter_backends = (OrderingFilter, SearchFilter, )
    ordering_fields = ('score', 'rating', 'created')
    # ordering = ('created',)
    search_fields = ('fullname', 'owner__username')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class ClapList(generics.ListCreateAPIView):
    queryset = Clap.objects.all()
    serializer_class = ClapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ClapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clap.objects.all()
    serializer_class = ClapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class SocialNetworkList(generics.ListCreateAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned Users to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/users?username=tony
        """
        queryset = SocialNetwork.objects.all()
        username = self.request.query_params.get('username', None)
        userqueryset = User.objects.all()
        users = userqueryset.filter(username=username)
        if len(users) and username is not None:
            queryset = queryset.filter(owner=users[0])
        return queryset

class SocialNetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class TShirtList(generics.ListCreateAPIView):
    # queryset = TShirt.objects.all()
    serializer_class = TShirtSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned Users to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/tshirts?code=1234
        """
        queryset = TShirt.objects.all()
        code = self.request.query_params.get('code', None)
        if code is not None:
            queryset = queryset.filter(code=code)
        return queryset

class TShirtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TShirt.objects.all()
    serializer_class = TShirtSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class SnippetList(generics.ListCreateAPIView):
    # queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    pagination_class = SnippetPagination

    filter_backends = (OrderingFilter, )
    ordering = ('-created',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned Users to a given user,
        by filtering against a `username` query parameter in the URL.
        http://example.com/api/users?username=tony
        """
        queryset = Snippet.objects.all()
        username = self.request.query_params.get('username', None)
        userqueryset = User.objects.all()
        users = userqueryset.filter(username=username)
        if len(users) and username is not None:
            queryset = queryset.filter(owner=users[0])
        return queryset

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminUser)

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminUser)

class MessageList(generics.ListCreateAPIView):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = Message.objects.all()
        sender = self.request.query_params.get('sender', None)
        receiver = self.request.query_params.get('receiver', None)
        if sender is not None:
            # queryset = queryset.filter(Q(sender=sender) | Q(receiver=receiver))
            queryset = queryset.filter(sender=sender)
        if receiver is not None:
            queryset = queryset.filter(receiver=receiver)
        return queryset

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'profiles': reverse('profile-list', request=request, format=format),
        'socialnetworks': reverse('socialnetwork-list', request=request, format=format),
        'tshirts': reverse('tshirt-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'stocks': reverse('stock-list', request=request, format=format),
        'messages': reverse('message-list', request=request, format=format),
        'claps': reverse('clap-list', request=request, format=format)
    })

@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_user(request):
    print("create_user")
    pin = request.data['pin']

    queryset = Stock.objects.all()
    queryset = queryset.filter(pin=pin)
    print(len(queryset))
    if(len(queryset) == 1):
        stock = queryset[0]
        print(stock.pin)

        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            print("valid")
            serialized.save()

            user = auth.authenticate(username=request.data['username'], password=request.data['password']);
            if user is not None:
                print("nice and easy")
                tshirt = TShirt(owner=user, message="", color=stock.color, size=stock.size, code=stock.code)
                profile = Profile(owner=user, email=request.data['email'], info="Please complete your profile")
                tshirt.save()
                profile.save()
                stock.delete()

                #test email
                send_html_mail('Welcome to DirStuff', 'Welcome message...', profile.email)
                #end test

            return Response({'response': 'ok'})
        else:
            print("no no")
            return Response({'response': 'bad'})
    else:
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            print("valid")
            serialized.save()

            user = auth.authenticate(username=request.data['username'], password=request.data['password']);
            if user is not None:
                print("nice and easy two")
                print('email:'+request.data['email'])
                profile = Profile(owner=user, email=request.data['email'], info="Please complete your profile")
                profile.save()

                #test email
                send_html_mail('Welcome to DirStuff', 'Welcome message...', profile.email)
                #end test

            return Response({'response': 'ok'})
        else:
            print("no no two")
            return Response({'response': 'bad'})

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def update_user(request):

    user = request.user
    user.set_password(request.data['password'])
    user.save()
    update_session_auth_hash(request, request.user)

    #email test
    queryset = Profile.objects.all()
    queryset = queryset.filter(owner=user)
    email = queryset[0].email
    print(email)
    send_html_mail('Password change', 
                   'Your DirStuff password have been changed. Visit our website: http://www.dircoolstuff.com/dir', 
                   email)
    #end test

    return Response({'response': 'ok'})

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def qr_generate(request):
    print('qr_generate')
    print(request.user.username)
    qrname = uuid.uuid4()
    tshirt = TShirt(owner=request.user, message="", color="black", size="M", code=qrname)
    tshirt.save()
    data = str(urllib.parse.quote('http://www.dircoolstuff.com/dir/#/tshirts/', safe=':/#-')) + str(qrname)
    print(data)

    # img = qrcode.make(data)
    img = pyqrcode.create(data)
    img = img.svg('webapps/dir/images/' + str(qrname) + '.svg', scale=8)
    # img.save('images/' + str(qrname) + '.svg')

    id = request.data['id']
    profile = Profile.objects.get(pk=id)
    profile.qrcode = str(qrname) + '.svg'
    profile.save()

    return Response({'response': 'ok', 'qrfilename': str(qrname) + '.svg'})

@api_view(['PUT'])
@permission_classes((permissions.IsAuthenticated, IsOwnerOrReadOnly))
def update_profile(request):
    id = request.data['id']
    info = request.data['info']
    rating = request.data['rating']
    score = request.data['score']
    fullname = request.data['fullname']
    email = request.data['email']
    profile = Profile.objects.get(pk=id)
    if (profile):
        profile.info = info
        profile.rating = rating
        profile.score = score
        profile.fullname = fullname
        profile.email = email
        profile.save()
        
        #test email
        send_html_mail('Update Profile', 'Your DirStuff profile have been updated', profile.email)
        #end test

        return Response({'response': 'ok'})
    return Response({'response': 'bad'})

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated, ))
def clap_profile(request):
    id = request.data['id']
    test = json.loads(request.data['test'])
    profile = Profile.objects.get(pk=id)
    if(profile):
        queryset = Clap.objects.all()
        claps = queryset.filter(profile=profile)
        exist = claps.filter(username=request.user.username)
        # queryset = queryset.filter(Q(profile=profile) & Q(username=request.user.username))
        if exist.count() == 0 and test == False:
            clap = Clap(profile=profile, username=request.user.username)
            clap.save()
            profile.score = claps.count()
            profile.save()

            # test email
            send_html_mail('Claps', 'Your DirStuff profile received a new clap', profile.email)
            # end test

        if exist.count() == 0 and test == True:
            return Response({'response': 'yes'})
 
        if exist.count() > 0 and test == True:
            return Response({'response': 'not'})

        return Response({'response': profile.score})

    return Response({'response': 'bad'})