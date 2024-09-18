from django.shortcuts import render, get_object_or_404, redirect  # Importa funções para renderizar templates, buscar objetos ou retornar um erro 404 e redirecionar URLs
from .models import Post  # Importa o modelo Post para manipulação de dados dos posts
from .forms import PostForm  # Adiciona o formulário PostForm se estiver usando um para criação/edição de posts

def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')  # Obtém todos os posts do banco de dados, ordenados da mais recente para a mais antiga
    return render(request, 'blog/lista_posts.html', {'posts': posts})  # Renderiza o template 'lista_posts.html' e passa a lista de posts como contexto

def detalhe_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Busca o post pelo id, ou retorna um erro 404 se o post não existir
    return render(request, 'blog/detalhe_post.html', {'post': post})  # Renderiza o template 'detalhe_post.html' com os dados do post específico

def criar_post(request):
    if request.method == 'POST':  # Verifica se o método da requisição é POST (enviando dados do formulário)
        form = PostForm(request.POST)  # Cria uma instância de PostForm com os dados enviados no POST
        if form.is_valid():  # Valida o formulário
            post = form.save()  # Salva o novo post no banco de dados
            return redirect('lista_posts')  # Redireciona o usuário para a lista de posts após salvar
    else:
        form = PostForm()  # Se não for uma requisição POST, cria um formulário vazio para preenchimento
    return render(request, 'blog/criar_post.html', {'form': form})  # Renderiza o template 'criar_post.html' com o formulário para criar um novo post



# View (V): A camada "View" em Django é responsável por processar as requisições e retornar respostas. Isso está sendo feito no arquivo views.py,
# onde você define as funções ou classes que gerenciam o que será exibido ao usuário quando ele acessar uma determinada URL.