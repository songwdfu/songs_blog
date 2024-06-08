from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class PostList(generic.ListView):
      # choose all published posts, order desc 
      queryset = Post.objects.filter(status=1).order_by('-created_on')
      template_name = 'index.html'
      
class PostDetail(generic.DetailView):
      model = Post
      template_name = 'post_detail.html'

@login_required
def create_post(request):
      if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                  post = form.save(commit=False)
                  post.author = request.user
                  post.save()
                  messages.success(request, f'Post successful: {post}')
                  return redirect('home')
            else:
                  messages.error(request, f'Post unsuccessful: {form.errors}')
      else:
            form = PostForm()
      return render(request, 'create_post.html', {'form': form})