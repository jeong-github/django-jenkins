from django.shortcuts import render
from .models import Post  # Import the Post model
from content.models import Feed


def index(request):
    feed_list = Feed.objects.all()
    return render(request, 'chanDjango/main.html', context={'feed_list': feed_list})



#from django.shortcuts import render
#from .models import Post  # Import the Post model
#
#def index(request):
#    posts = Post.objects.all()  # Fetch all posts from the database
#    return render(request, 'chanDjango/main.html', {'posts': posts})  # Render the 'Changjango/Main.html' template
