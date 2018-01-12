from rest_framework import serializers
from snippets.models import Snippet, TShirt, Profile, SocialNetwork, Stock, Message, Clap, Follower, Notification, MediaFile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    tshirts = serializers.HyperlinkedRelatedField(many=True, view_name='tshirt-detail', read_only=True)
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    profiles = serializers.HyperlinkedRelatedField(many=True, view_name='profile-detail', read_only=True)
    socialnetworks = serializers.HyperlinkedRelatedField(many=True, view_name='socialnetwork-detail', read_only=True)
    messages = serializers.HyperlinkedRelatedField(many=True, view_name='message-detail', read_only=True)

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'tshirts', 'snippets', 'profiles', 'socialnetworks', 'messages')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followers = serializers.HyperlinkedRelatedField(many=True, view_name='follower-detail', read_only=True)
    claps = serializers.HyperlinkedRelatedField(many=True, view_name='clap-detail', read_only=True)
    notifications = serializers.HyperlinkedRelatedField(many=True, view_name='notification-detail', read_only=True)

    class Meta:
        model = Profile
        fields = ('url', 'id', 'created', 'owner', 'info', 'rating', 'score', 'avatar', 'fullname', 'email', 'phone', 'qrcode', 'claps', 'followers', 'notifications', 'confVisible', 'confEmailVisible', 'confReceiveMails')


class ClapSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.owner.username')

    class Meta:
        model = Clap
        fields = ('url', 'id', 'created', 'profile', 'username')

class FollowerSerializer(serializers.HyperlinkedModelSerializer):
    profileUserName = serializers.ReadOnlyField(source='profile.owner.username')
    profileFullName = serializers.ReadOnlyField(source='profile.fullname')
    profileInfo = serializers.ReadOnlyField(source='profile.info')
    profileAvatar = serializers.ReadOnlyField(source='profile.avatar.url')
    profileId = serializers.ReadOnlyField(source='profile.id')

    class Meta:
        model = Follower
        fields = ('url', 'id', 'created', 'username', 'userId', 'fullName', 'avatar', 'info', 'profileId', 'profileUserName', 'profileFullName', 'profileInfo', 'profileAvatar', 'currentFollowed')

class NotificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Notification
        fields = ('url', 'id', 'created', 'info', 'type', 'readed', 'profileId', 'profileFullName', 'profileAvatar')

class SocialNetworkSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SocialNetwork
        fields = ('url', 'id', 'owner', 'name', 'type', 'url')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'created', 'owner', 'title', 'body')

class MediaFileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MediaFile
        fields = ('url', 'id', 'owner', 'title', 'banner')

class TShirtSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TShirt
        fields = ('url', 'id', 'owner', 'message', 'color', 'size', 'code')

class StockSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stock
        fields = ('url', 'id', 'color', 'size', 'code', 'pin')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ('url', 'id', 'owner', 'created', 'sender', 'receiver', 'subject', 'body', 'readed')