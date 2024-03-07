from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def index(request):
<<<<<<< HEAD
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
=======
  return render(request, "blog/index.html")

>>>>>>> 4d9b0b277bd9b844df3ed26c6b05376cadf9b2cd
