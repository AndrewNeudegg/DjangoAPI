from __future__ import unicode_literals  # -*- coding: utf-8 -*-
from django.shortcuts import render  # Import DJANGO Renderer for routing.
from django.contrib.auth.models import User, Group  # Import our defined login auth model, Ref: http://www.django-rest-framework.org/tutorial/quickstart/#views
from django.http import HttpResponse
from rest_framework.filters import OrderingFilter, SearchFilter, DjangoFilterBackend  ### Important - Load the django filters. Ref: http://www.django-rest-framework.org/api-guide/filtering/
from rest_framework import permissions, viewsets  # Import concept of viewsets and permission to inherit from.
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope  # Import concepts of tokens and token scope.
from django.http import HttpResponse
from django.template import Context, loader  
from serializers import(
    RandomBlockSerializer,
    SensorDataBlockSerializer,
    PartnerBlockSerializer,
    UpdateBlockSerializer,
    UserSerializer,  # Predefined auth serializer.
    GroupSerializer,  # Predefined auth serializer.
)  # Import all serializers.
from models import(
    RandomBlock,
    SensorDataBlock,
    PartnerBlock,
    UpdateBlock,
)  # Import all Block models.



###   API endpoint that allows RandomBlocks to be viewed or edited.
class RandomBlockViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]  # OAuth black magic
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        )  # Enable Django filters.
    queryset = RandomBlock.objects.all()
    serializer_class = RandomBlockSerializer


###   API endpoint that allows SensorDataBlocks to be viewed or edited.
class SensorDataBlockViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]  # OAuth black magic
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        )  # Enable Django filters.
    queryset = SensorDataBlock.objects.all()
    serializer_class = SensorDataBlockSerializer


###   API endpoint that allows SensorDataBlocks to be viewed or edited.
class PartnerBlockBlockViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]  # OAuth black magic   
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        )  # Enable Django filters. 
    queryset = PartnerBlock.objects.all()
    serializer_class = PartnerBlockSerializer


###   API endpoint that allows UpdateBlocks to be viewed or edited.
class UpdateBlockBlockViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]  # OAuth black magic
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        )  # Enable Django filters.
    queryset = UpdateBlock.objects.all()
    serializer_class = UpdateBlockSerializer



### The following classes permit the login auth-api. Heavily modified.
### Reference: http://www.django-rest-framework.org/tutorial/quickstart/#views
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [TokenHasReadWriteScope]  # OAuth black magic
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        )  # Enable Django filters.
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [TokenHasReadWriteScope]  # OAuth black magic
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        )  # Enable Django filters.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



### With a lot of help from: http://stackoverflow.com/questions/11302829/custom-django-404-error
### Turns out azure doesn't cope so well with the templates directory
### So the best soloution I've found is to generate the
### response within the view method. 
### Took this post to get it working: http://stackoverflow.com/questions/16367374/django-raising-404-with-a-message
##
# Handle 404 Errors
# @param request WSGIRequest list with all HTTP Request
def error404(request):
    msg = 'Error 404'
    return HttpResponse(msg, status=404)
    ##
    
# Handle 404 Errors
# @param request WSGIRequest list with all HTTP Request
def error500(request):
    msg = 'Error 500'
    return HttpResponse(msg, status=500)