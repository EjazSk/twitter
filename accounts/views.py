from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

def view_user(request,username):
    user = get_object_or_404(User,username=username)
    print(user)
    context = {'user':user}
    return render(request,'profile.html', context)

    