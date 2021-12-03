from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from core.models import DailyMontage, MontagePaid




@login_required()
def profile(request, username):
    dailys = DailyMontage.objects.filter(user__username=username).all().order_by('-date')
    montages = MontagePaid.objects.filter(montage__user__username=username).all().order_by('-date')
    context = locals()
    return render(request, 'accounts.html', context)


def logout_view(request):
    logout(request)
    return redirect('core:home')
