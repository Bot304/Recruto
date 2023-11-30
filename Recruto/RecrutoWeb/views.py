from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    name = request.GET.get("name","Recruto!")
    message = request.GET.get("message","Давай дружить")
    data = {"name": name, "message": message}
    return render(request, "index.html", context=data)
 