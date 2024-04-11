from rest_framework import serializers
from emails.models import Subscription
from emails.utils import validators


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    def validate_email(self, email):
        if not validators.email(email):
            raise serializers.ValidationError("E-mail inválido") 
        return email