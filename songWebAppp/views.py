from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from songWebAppp import models
user_list=[
    {"user":"song","pwd":"123"},
    {"user":"jiu","pwd":"456"},
]
def index(request):
    #return HttpResponse("Hello song, welcome to django")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        '''Page Web statique'''
        #print(username, password)
        '''without bdd (M)TV'''
        #temp={"user":username,"pwd":password}
        #user_list.append(temp)
        '''MTV'''
        models.UserInfo.objects.create(user=username, pwd=password) #ajouter donnes a bdd
    user_list=models.UserInfo.objects.all()
    return  render(request, "index.html", {"data":user_list}) #Package html