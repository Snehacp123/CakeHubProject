from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from myapp.models import Cake
from rest_framework import serializers
from rest_framework.decorators import action

class CakeboxSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Cake
        fields="__all__"

class CakeboxView(ViewSet):
    
    def list(self,request,*args,**kwargs):
        qs=Cake.objects.all()
        if "flavour" in request.query_params:
            flav=request.query_params.get("flavour")
            qs=qs.filter(flavour__iexact=flav)

        if "shape" in request.query_params:
            shp=request.query_params.get("shape")
            qs=qs.filter(shape__iexact=shp)
        serializer=CakeboxSerializer(qs,many=True) 
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=CakeboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cake.objects.get(id=id)
        serializer=CakeboxSerializer(qs)
        return Response(data=serializer.data)
 
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_obj=Cake.objects.get(id=id)
        serializer=CakeboxSerializer(instance=emp_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            Cake.objects.get(id=id).delete()
            return Response(data="deleted")
        except Exception:
            return Response(data="no matching record find")
        

    @action(methods=["get"],detail=False)
    def departments(self,request,*args,**kwargs):
        qs=Cake.objects.all().values_list("flavour",flat=True).distinct()
        return Response(data=qs)