from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('writers/', views.AuthorListView.as_view(), name='writers'),
    path('writer/<int:pk>', views.author_detail_view, name='writer-detail'),
    path('submit/', views.ArticleCreate, name='sumbit-article'),
]