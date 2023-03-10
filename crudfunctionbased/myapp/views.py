from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentForm

# Create your views here.

# these function to add data and show all information
def addshow(request):    
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, email=em, password=pw) 
            reg.save() 
            fm = StudentForm() 
    else: 
        fm = StudentForm()            
    stud = Student.objects.all()
    return render(request, "myapp/addandshow.html", {"form":fm, "stud":stud})  

# this function will update/delete
def updatedata(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save() 
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentForm(instance=pi) 

    return render(request, "myapp/updatestudent.html", {"form":fm})  
 
# this function will delete
def deletedata(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()       

        return HttpResponseRedirect('/')