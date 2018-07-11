from django.shortcuts import render

#the function returns;
def getpage(request):
    return render(request,'index.html')

#the view function returns userprofile.html to browser
def getprofilepage(request):
    return render(request,'userprofile.html')

#this views function will save user profile model object to data base
def saveUserProfile(request):
    userid=request.Post['uid']
    username=request.Post['uname']
    password=request.Post['pwd']
    email=request.Post['email']
    up=UserProfile(email=email,userid=userid,password=password,username=username)
    up.save()
    return render(request,'index.html')
