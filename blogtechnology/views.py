from django.shortcuts import render

from blogtechnology.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request , 'blogtechnology/magazine-template.html' , context)