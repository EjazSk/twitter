from django.shortcuts import render, redirect
from .models import TweetModal
from .forms import TweetModalForm
# Create your views here.
def home(request):
    form = TweetModalForm(request.POST or None)
    tweets = TweetModal.objects.all()
    q = request.GET.get('q')
    if q:
        tweets = TweetModal.objects.filter(content__icontains=q)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    form = TweetModalForm(request.POST or None)
    context = {'tweets':tweets,'form':form}
    return render(request, 'home.html', context)

