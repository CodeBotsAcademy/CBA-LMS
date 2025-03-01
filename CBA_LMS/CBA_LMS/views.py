from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def homepage(request):
    context = {
        'image' : 'media/teacher.png'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')