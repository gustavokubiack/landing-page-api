from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework import status
from emails.serializers import SubscriptionSerializer
from app import settings
from emails.services.send_emails.send_emails import SendEmail


class Subscribe(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            service = SendEmail(serializer.data)
            service.send()
            return Response({"message": "Inscrição realizada com sucesso!"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)