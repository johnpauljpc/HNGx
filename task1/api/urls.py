from django.urls import path
from .views import InfoAPIView

urlpatterns = [
    path("api/", InfoAPIView.as_view(), name="info")
]