from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

from reviews.models import Author, Article, Comment
from django.views import generic

def index(request):

    num_articles = Article.objects.all().count()

    last_article = Article.objects.latest('created')

    context = {
        'num_articles': num_articles,
        'last_article': last_article
    }

    return render(request, 'index.html', context=context)

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 10

class ArticleDetailView(generic.DetailView):
    model = Article

class AuthorListView(generic.ListView):
    model = Author

def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    articles = Article.objects.filter(author__pk=pk)
    context = {
        'author': author,
        'articles': articles
    }
    return render(request, 'reviews/author_detail.html', context=context)



