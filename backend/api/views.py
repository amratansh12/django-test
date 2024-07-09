from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Project

# Create your views here.
def home(request):
    return HttpResponse("This is working")

class ProjectViewsets(viewsets.ViewSet):
    permissions_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    
    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request):
        pass

    def update(self, request):
        pass

    def destroy(self, request):
        pass