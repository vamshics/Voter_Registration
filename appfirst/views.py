from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request,"template.html")
def hello1(request):
    return render(request,"thankyou.html")
