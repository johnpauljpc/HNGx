from django.urls import path
from . import views

urlpatterns = [
    path("", views.PersonListView.as_view(), name="person-list"),
    
    path("create/", views.PersonCreateView.as_view(), name="person-create"),
    path("detail/<int:pk>/", views.PersonDetailView.as_view(), name="person-detail"),
    path("update/<int:pk>/", views.PersonUpdateView.as_view(), name="person-update"),
    path("delete/<int:pk>/", views.PersonDeleteView.as_view(), name="person-delete"),
]

