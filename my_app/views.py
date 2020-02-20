from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    #return HttpResponse("Hello, Welcome to my profile") 


    return render(request, 'my_app/index.html')

def about(request):
    
    return render(request, 'my_app/about.html')



def contact_view(request):
    
    return render(request, 'my_app/contact.html')



def skill_view(request):
    
    return render(request, 'my_app/skill.html')



def exp_view(request):
    
    return render(request, 'my_app/experience.html')