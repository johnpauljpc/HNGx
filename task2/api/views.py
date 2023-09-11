from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                      UpdateAPIView, RetrieveAPIView, DestroyAPIView)

from .models import Person
from .serializers import PersonSerializer

### Views

# View for adding a new person.
class PersonCreateView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# View for listing all the persons
class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# View for fetching details of a person.
class PersonDetailView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# View for modifying details of an existing person
class PersonUpdateView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# View for removing a person.
class PersonDeleteView(DestroyAPIView):
    queryset = Person.objects.all()
    