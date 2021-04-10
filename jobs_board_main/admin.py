from django.contrib import admin

# Register your models here.
from .models import Job, Subscriber, Subscription

admin.site.register(Job)
admin.site.register(Subscriber)
admin.site.register(Subscription)
