
from django.shortcuts import render,redirect

from movieApp.forms import movieform
from .models import movie
from .forms import movieform

# Create your views here.
def home(request):
    m=movie.objects.all()
    return render(request,'home.html',{'m':m})

def details(request,movie_id):
    data=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'data':data})

def edit(request,movie_id):
    data=movie.objects.get(id=movie_id)
    form=movieform(request.POST or None,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'data':data})

def delete(request,movie_id):
    data=movie.objects.get(id=movie_id)
    if request.method=='POST':
        data.delete()
        return redirect('/')
    return render(request,'delete.html',{'data':data})

def add_movie(request):
        if request.method=='POST':
            name=request.POST.get('name')
            year=request.POST.get('year')
            desc=request.POST.get('desc')
            img=request.FILES['img']
            movie_var=movie(name=name,year=year,desc=desc,img=img)
            movie_var.save()
            return redirect('/')
        return render(request,'add.html')