from django.shortcuts import render,redirect

# Create your views here.
def input(request):
    return redirect("/admin/input/attendance/add/")
