from django.shortcuts import render

# Create your views here.

def calendario(request):
    return render(request, 'calendario.html')

def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def noticias(request):
    return render(request, 'noticias.html')

def programas(request):
    return render(request, 'programas.html')