from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/main.html')

def learning(request):
    return render(request, "learning/learning.html")
