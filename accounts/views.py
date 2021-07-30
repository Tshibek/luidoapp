from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('core:home')