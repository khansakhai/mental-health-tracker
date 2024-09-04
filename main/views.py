from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152462',
        'name': 'Khansa Khairunisa',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)