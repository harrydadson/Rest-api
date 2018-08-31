from django.shortcuts import render
from .serializers import BucketlistSerializer
from .models import Bucketlist
from rest_framework import generics

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    #define our api
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        #save the post data when creating a new bucketlist
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
