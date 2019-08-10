from django.shortcuts import render,redirect

# Create your views here.
def input(request):
    return redirect("/admin/input/attendance/add/")
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
