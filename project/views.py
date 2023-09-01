from django.shortcuts import render
from.models import shop
from.models import contact as cn


# Create your views here.
def contact(request):
    n=request.GET.get("name")
    e=request.GET.get("email")
    m=request.GET.get("msg_subject")
    ph=request.GET.get("phone_number")
    com=request.GET.get("comment")
    if(n and e and m and ph and com):
        cn.objects.create(name=n,email=e,msg_subject=m,phone_number=ph)
        return render(request,"project/s.html")
    
    return render(request,"project/contact.html")

def show(request,code):
    
    l=shop.objects.get(id=code)
    return render(request,"project/shop.html",context={"shop":l})
    
def project(request):
    l=shop.objects.filter(noe=1)
    return render(request,"project/index.html",context={"shop":l})

def about(request):
    return render(request,"project/about.html")

def instructor(request):
    return render(request,"project/instructor.html")
def courses(request):
    return render(request,"project/courses.html")
