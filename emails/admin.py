from django.contrib import admin
from emails.models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fields = ("name", "email")