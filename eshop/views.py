from django.shortcuts import render,redirect
from django.http import HttpResponse
from eshop.forms import StudentForm
from .models import Student
# Create your views here.
def display(request):
    if request.method=="POST":
        st=StudentForm(request.POST)
        if(st.is_valid()):
            st.save()
            return redirect("/show")
    st=StudentForm()
    return render(request,"index.html",{"student":st})

def show(request):
    students=Student.objects.all()
    return render(request,"show.html",{"students":students})

def edit(request,id):
   student=Student.objects.get(id=id)
   return render(request,"edit.html",{"student":student})

def update(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("name")
        marks=request.POST.get("marks")
        student.name=name
        student.marks=marks
        student.save()
        return redirect("/show")
    return render(request,"edit.html",{"student":student})

    


def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/show")


def setcookie(request):
    response=HttpResponse("Cookie has been set")
    response.set_cookie("username","john")
    return response

def getcookies(request):
    username=request.COOKIES["username"]
    return HttpResponse(username)

def delete_cookie_view(request):
    response=HttpResponse("Cookie has been deleted")
    response.delete_cookie("username")
    return response
    
def setsession(request):
    request.session["username"]="john"
    return HttpResponse("Session is set")

def getsession(request):
    username=request.session["username"]
    return HttpResponse(username)

def delete_session(request):
    del request.session["username"]
    return HttpResponse("Session is deleted")