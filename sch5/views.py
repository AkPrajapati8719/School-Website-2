from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def event(request):
    return render(request,'event.html')
def contact(request):
    return render(request,'contact.html')

# Create your views here.
