from django.shortcuts import render

#the function returns;
def getpage(request):
    return render(request,'index.html')

#the view function returns userprofile.html to browser
def getprofilepage(request):
    return render(request, 'userprofile.html')

#this views function will save user profile model object to data base
def save UserProfile(request):
    userid=request.post['uid']
    username=request.post['uname']
    password=request.post['pwd']
    email=request.post['email']

