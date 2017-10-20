from django.contrib import admin

from snippets.models import Snippet, TShirt, Profile

# Register your models here.
admin.site.register(Snippet)
admin.site.register(TShirt)
admin.site.register(Profile)
