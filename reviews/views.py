from django.shortcuts import render

# Create your views here.

from reviews.models import Author, Article, Comment

def index(request):

    num_articles = Article.objects.all().count()

    last_article = Article.objects.latest('created')

    context = {
        'num_articles': num_articles,
        'last_article': last_article
    }

    return render(request, 'index.html', context=context)



