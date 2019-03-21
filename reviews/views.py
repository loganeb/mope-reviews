from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required

# Create your views here.

from reviews.models import Author, Article, Comment
from reviews.forms import ArticleForm

def index(request):

    num_articles = Article.objects.all().count()

    last_article = Article.objects.latest('created')

    context = {
        'num_articles': num_articles,
        'last_article': last_article,
    }

    return render(request, 'index.html', context=context)

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 25

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


@permission_required('reviews.can_mark_returned')
def ArticleCreate(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            author = request.user
            new_article = Article(title=title, body=body, author=author)
            new_article.save()
