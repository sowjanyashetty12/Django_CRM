from django.shortcuts import render,redirect
from django.contrib.auth import login ,authenticate,logout
from django.contrib import messages
from .forms import SignUpForm , AddNewRecordForm
from .models import Record
# Create your views here.
def home(request):
    #things to display from model while logged in
    records=Record.objects.all()
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in")
            return redirect("home")
        else:
           messages.error(request,"invalid username or password")
           return redirect("home")
    else:
        return render(request,"home.html",{'records':records})
def logout_user(request):
    logout(request)
    messages.success(request,"You've been logged out")
    return render(request,"home.html")
def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Logged in")
            return redirect("home")

    else:
        form=SignUpForm()
    return render(request,"register.html",{'form':form})
def customer_record(request,pk):
    if request.user.is_authenticated:
        record=Record.objects.get(id=pk)
        return render(request,"record.html",{'record':record})
    else:
        messages.error(request,"login required")
        return redirect("home")
def delete_record(request,pk):
    if request.user.is_authenticated:
        deleteitem=Record.objects.get(id=pk)
        deleteitem.delete()
        messages.success(request,f"ID{pk} has been deleted ")
        return redirect("home")
    else:
        messages.error(request,"you need to login to do this action")
        return redirect("home")
def add_record(request):
    recordform=AddNewRecordForm(request.POST or None)
    if request.user.is_authenticated:
       if request.method=="POST":
         if recordform.is_valid():
            addrecord=recordform.save()
            messages.success(request, "Record Added...")
            return redirect("home")
       return render(request,"add_record.html",{'recordform':recordform})
    else:
         messages.error(request,"you need to login to do this action")
         return redirect("home")


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        updateform=AddNewRecordForm(request.POST or None , instance=current_record)
        if request.method=="POST":
            if updateform.is_valid():
                updateform.save()
                return redirect("home")
        else:
            return render(request,"updateform.html",{"updateform":updateform})