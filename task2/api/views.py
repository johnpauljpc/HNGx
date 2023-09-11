from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .models import Person
from .serializers import PersonSerializer

### Views

# View for listing and creating users.
class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# View for retrieving, updating, and deleting a given user
class PersonRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

