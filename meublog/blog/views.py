from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # Adicione esta linha se você estiver usando um formulário

def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')  # Ordena os posts pela data de publicação
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalhe_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalhe_post.html', {'post': post})

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Certifique-se de ter um formulário no forms.py
        if form.is_valid():
            post = form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/criar_post.html', {'form': form})
