from django.contrib import admin
from django.urls import path, include
from apps.ticket import urls as ticket_urls

urlpatterns = [
    path('ticket/', include(ticket_urls)),
    path('admin/', admin.site.urls),
]
