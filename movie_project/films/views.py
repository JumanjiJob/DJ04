from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

def home(request):
    return render(request, 'films/home.html')

def review(request):
    films = News_post.objects.all()
    return render(request, 'films/review.html', {'films': films})

def create_review(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были зполнены некорректно"
    form = News_postForm()
    return render(request, 'films/create_review.html', {'form': form, 'errors': error})
