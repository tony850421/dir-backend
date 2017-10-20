from rest_framework import serializers
from snippets.models import Snippet, TShirt, Profile, SocialNetwork, Stock, Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    tshirts = serializers.HyperlinkedRelatedField(many=True, view_name='tshirt-detail', read_only=True)
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    profiles = serializers.HyperlinkedRelatedField(many=True, view_name='profile-detail', read_only=True)
    socialnetworks = serializers.HyperlinkedRelatedField(many=True, view_name='socialnetwork-detail', read_only=True)

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'tshirts', 'snippets', 'profiles', 'socialnetworks')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = ('url', 'id', 'created', 'owner', 'info', 'rating', 'score', 'avatar')

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

    class Meta:
        model = Message
        fields = ('url', 'id', 'created', 'sender', 'receiver', 'subject', 'body', 'readed')