from django.db import models
import uuid

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "webapps/dir/images/{}.{}".format(uuid.uuid4(), extension)

class Profile(models.Model):
    owner = models.ForeignKey('auth.User', related_name='profiles', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    info = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    avatar = models.ImageField(upload_to=scramble_uploaded_filename, null=True, blank=True)

    class Meta:
        ordering = ('created',)

class SocialNetwork(models.Model):
    owner = models.ForeignKey('auth.User', related_name='socialnetworks', on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='fb')
    url = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('type',)

class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()

    class Meta:
        ordering = ('created',)

class TShirt(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tshirts', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100, blank=True, default='')
    color = models.TextField()
    size = models.TextField()
    code = models.TextField()

    class Meta:
        ordering = ('created',)

class Stock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    color = models.TextField()
    size = models.TextField()
    code = models.TextField()
    pin = models.TextField()

    class Meta:
        ordering = ('created',)

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    sender = models.TextField()
    receiver = models.TextField()
    subject = models.TextField()
    body = models.TextField()
    readed = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)