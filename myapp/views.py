from django.shortcuts import render,redirect
from django import forms
from django.views.generic import View
from myapp.models import Cake
from django.contrib.auth.models import User







class CakeForm(forms.ModelForm):

    class Meta:
        model=Cake
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "prize":forms.NumberInput(attrs={"class":"form-control"}),
            "shape":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.TextInput(attrs={"class":"form-control"}),
            "number":forms.NumberInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "cake_image":forms.FileInput(attrs={"class":"form-control"}),

        }

class RegisterationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})


        }


class CakeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CakeForm()
        return render(request,"cake-add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=CakeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cake-list")
        return render(request,"cake-add.html",{"form":form})
    
class CakeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Cake.objects.all()
        return render(request,"cake-list.html",{"cakes":qs}) 

class CakeDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Cake.objects.get(id=id)
        return render(request,"cake-details.html",{"cake":qs})
    
class CakeDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Cake.objects.get(id=id).delete()
        return redirect("cake-list")
    
class CakeEditview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cake.objects.get(id=id)
        form=CakeForm(instance=cake)

        
        return render(request,"cake-edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cake.objects.get(id=id)
        form=CakeForm(instance=cake,data=request.POST,files=request.FILES)
        
        if form.is_valid():
            
            form.save()
            return redirect("cake-details",pk=id)
        
        return render(request,"cake-edit.html",{"form":form})
    

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegisterationForm()
        return render(request,"register.html",{"form":form})