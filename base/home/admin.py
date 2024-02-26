from django.contrib import admin
from . models import BookingUser, Feedback

# Register your models here.

admin.site.register(BookingUser)
admin.site.register(Feedback)