from django.urls import path
from . import views

urlpatterns = [
    # url path for listing and creating users.
    path("", views.PersonListCreateView.as_view(), name="person-list-create"),

    # url path for retrieving, updating, and deleting a given user
    path("<int:pk>/", views.PersonRUDView.as_view(), name="person-detail"),
]

