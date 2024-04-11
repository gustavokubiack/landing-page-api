
from django.contrib import admin
from django.urls import path
from emails.views import Subscribe

urlpatterns = [
    path("admin/", admin.site.urls),
    path('send-email/', Subscribe.as_view(), name='send-email'),
]
