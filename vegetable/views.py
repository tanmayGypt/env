from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def receipes(request):
    if(request.method=="POST"):
        
        data=request.POST
        receipe_image=request.FILES['receipe_image']
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        
        
        Reciepe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
        )
        return redirect("/receipes/")
    
    AllData=Reciepe.objects.all()
    print(request.GET.get('search'))
    print(request.GET.get('search'))
    if request.GET.get("search"):
        
        AllData=AllData.filter(receipe_name__icontains = request.GET.get('search'))
        
    context={'receipes':AllData}
    return render(request,'index.html',context)

def home(request):
    return render(request, "home.html")

def delete_receipe(request, id):
    q=Reciepe.objects.filter(id=id).delete()
    return redirect("/receipes/")


        

def receipe_updated(request, id):
    
    if(request.method=='POST'):
        data=request.POST
        receipe_image=request.FILES['receipe_image']
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        
        r= Reciepe.objects.get(id=id)
        r.receipe_name=receipe_name
        r.receipe_description=receipe_description
        r.receipe_image=receipe_image
        r.save()
               
        return redirect("/receipes/")
    return render(request, 'update.html')