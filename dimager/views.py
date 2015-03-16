from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):
    context = {'name' : request.user}
    return render(request, 'profile.html', context)
