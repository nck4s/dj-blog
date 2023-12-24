from django.shortcuts import render


posts = [
    {
        'author': 'Nika',
        'title': 'Blog post 1',
        'content': 'This is my blog',
        'date_posted': '5th March, 2021', 
    },
    {
        'author': 'John',
        'title': 'Blog post 2',
        'content': 'This is his blog post',
        'date_posted': '9th March, 2022', 
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
