from django.contrib import admin
from .models import Room, Message

# Register your models here.

# need to register database models to admin page
admin.site.register(Room)
admin.site.register(Message)