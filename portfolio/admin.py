from django.contrib import admin
from .models import BookingRequest, ContactRequest

admin.site.register(BookingRequest)
admin.site.register(ContactRequest)
