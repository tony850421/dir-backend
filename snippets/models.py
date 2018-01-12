from django.db import models
import uuid

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "webapps/dir/images/{}.{}".format(uuid.uuid4(), extension)

class Profile(models.Model):
    owner = models.ForeignKey('auth.User', related_name='profiles', on_delete=models.CASCADE)

    email = models.EmailField(blank=False, default='')
    fullname = models.CharField(max_length=100, blank=True, default='')
    phone = models.TextField(default='+8613817991444')
    created = models.DateTimeField(auto_now_add=True)
    info = models.TextField(default='')
    rating = models.DecimalField(default=0.0, max_digits=4, decimal_places=2, editable=False)
    score = models.PositiveIntegerField(default=0, editable=False)
    avatar = models.ImageField(upload_to=scramble_uploaded_filename, default="images/default-user.png")
    qrcode = models.CharField(max_length=200, blank=True, default='')

    confVisible = models.BooleanField(default=True)
    confEmailVisible = models.BooleanField(default=True)
    confReceiveMails = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

class Clap(models.Model):
    profile = models.ForeignKey(Profile, related_name='claps', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)

class Follower(models.Model):
    profile = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='')
    fullName = models.CharField(max_length=100, blank=True, default='')
    avatar = models.CharField(max_length=100, blank=True, default='')
    info = models.TextField(default='')
    currentFollowed = models.BooleanField(default=False)
    userId = models.CharField(max_length=40, blank=True, default='')

    class Meta:
        ordering = ('-created',)

class Notification(models.Model):
    profile = models.ForeignKey(Profile, related_name='notifications', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    info = models.TextField(default='')
    type = models.CharField(max_length=100, blank=True, default='newfollower')
    readed = models.BooleanField(default=False)

    # profileUserName = models.CharField(max_length=100, blank=True, default='')
    profileFullName = models.CharField(max_length=100, blank=True, default='')
    profileAvatar = models.CharField(max_length=100, blank=True, default='')
    profileId = models.CharField(max_length=40, blank=True, default='')

    class Meta:
        ordering = ('-created',)

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

class MediaFile(models.Model):
    owner = models.ForeignKey('auth.User', related_name='mediafiles', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='file')
    banner = models.ImageField(upload_to=scramble_uploaded_filename, default="images/features-background.jpg")

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
    code = models.TextField(editable=False)
    pin = models.TextField(editable=False)

    class Meta:
        ordering = ('created',)

class Message(models.Model):
    owner = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    sender = models.TextField()
    receiver = models.TextField()
    subject = models.TextField()
    body = models.TextField()
    readed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)