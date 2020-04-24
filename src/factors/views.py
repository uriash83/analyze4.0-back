from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets , permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from collections import OrderedDict 

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import models
from . import serializers
from . import pagination

from .utils.calculate import formatDate
from math import exp


from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView , 
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView)


# class FactorListView(ListAPIView):
#     queryset = models.Factors.objects.all()
#     serializer_class = serializers.FactorsSerializer


# class FactorDetailView(RetrieveAPIView):
#     queryset = models.Factors.objects.all()
#     serializer_class = serializers.FactorsSerializer

# class FactorCreateView(CreateAPIView):
#     queryset = models.Factors.objects.all()
#     serializer_class = serializers.FactorsSerializer

# class FactorUpdateView(UpdateAPIView):
#     queryset = models.Factors.objects.all()
#     serializer_class = serializers.FactorsSerializer

# class FactorDeleteView(DestroyAPIView):
#     queryset = models.Factors.objects.all()
#     serializer_class = serializers.FactorsSerializer




class FactorsViewset(viewsets.ModelViewSet):
    queryset = models.Factors.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = serializers.FactorsSerializer
    
    # queryset = models.Factors.objects.all()
    # serializer_class = serializers.FactorsSerializer



    # def get_queryset(self):
    #     print('QUERYSET')
    #     return self.request.user.Factors.all()

    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)
    # FACTORS_GET 
    def list(self, request):
        
        
        
        #print(request.query_params.get('month') )
        # sprawdż czy jest w componencie PEC i zasysa dane 1,2,3 miesiące
        if request.query_params.get('month'):
            PECrangeDisplay = int(request.query_params.get('month'))
            queryset = models.Factors.objects.all().filter(user=request.user).order_by('-id')[:PECrangeDisplay]
            
            print(request.query_params)
            serializer = serializers.FactorsSerializer(queryset, many=True)
            return Response(OrderedDict([('data',serializer.data)]))
        # jeśli nie to jest w widoku RawData i zrów paginacje
        else:
            print(request.query_params)
            queryset = models.Factors.objects.all().filter(user=request.user)
            paginator = pagination.StandardResultsSetPagination()
            page_roles = paginator.paginate_queryset(queryset=queryset, request=request, view=self)
            print('LINK')
            print(paginator.get_html_context)
            #print(request.data)
            #print(request.user)
            serializer = serializers.FactorsSerializer(page_roles, many=True)
            return paginator.get_paginated_response(serializer.data) 
        

    # FACTOR_CREATE
    def create(self, request):
        #print(request.data['tss'])
        data_copy=request.data.copy()
        tss=int(data_copy['tss'])
        ctl = int(tss*(1-exp(-1/42))+128*exp(-1/42))
        atl = int(tss*(1-exp(-1/7))+164*exp(-1/7))
        #print(type(ctl),type(atl))
        tbs = ctl-atl
        data_copy['atl'] = str(atl)
        data_copy['ctl'] = str(ctl)
        data_copy['tbs'] = str(tbs)
        data_copy['date'] = formatDate(data_copy['date'])
        print(type(atl))
        print(data_copy['date'])
        serializer = serializers.FactorsSerializer(data=data_copy)
        
        #serializer = serializers.FactorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        #print(request.data)
        #print('PUT')
        dataUpdate = request.data
        dataUpdate['date'] = formatDate(dataUpdate['date'])
        #print (request.__dict__)
        # nie ważna jest kolejność w jakiej są dane , może być ich więcej , byle się zgadzały z modelem
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = serializers.FactorsSerializer(instance, data=dataUpdate, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 







        


