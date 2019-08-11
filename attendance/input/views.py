from django.shortcuts import render,redirect,HttpResponse
from .models import Attendance

# Create your views here.
def input(request):
    return redirect("/admin/input/attendance/add/")
def view(request):
    if request.method=="POST":
        classes=[]
        classes_a= Attendance.objects.filter(subs=request.POST.get("sub"))
        for class_a in classes_a:
            if class_a.date.month()==request.POST.get("month"):
                classes.append(class_a)
        total=0
        attended=0
        for c in classes:
            total+=1
            if c.status==True:
                attended+=1
        percentage=(attended/total)*100
        return render(request,"input/index.html",context={"classes":classes,"percentage":percentage})
    else:
        return render(request,"input/index.html")
@csrf_exempt
def webhook(request):
  if request.method == 'POST':
    repo = git.Repo('/home/aditjain/attendancet_tracker')
    repo.git.reset('--hard')
    repo.git.clean('-fdx')

    origin = repo.remotes.origin
    origin.pull()
    return HttpResponse("Success")
  else:
    return HttpResponse("Cool")
