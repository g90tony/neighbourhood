from django.contrib import admin
from .models import Business, Contact, Event, ImagePost, Neighbourhood, Profile, TextPost
# Register your models here.

admin.site.register(Business)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(ImagePost)
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(TextPost)