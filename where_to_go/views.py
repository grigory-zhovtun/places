from django.shortcuts import render

def places(request):
    return render(request, 'index.html')