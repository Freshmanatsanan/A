from django.shortcuts import render
from .models import Course
# Create your views here.

def A(request):
    courses = Course.objects.all()
    return render(request, 'A.html', {'courses': courses})
