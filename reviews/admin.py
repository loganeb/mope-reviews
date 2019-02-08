from django.contrib import admin

# Register your models here.
from reviews.models import Article, Comment, Author

admin.site.register(Comment)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

admin.site.register(Author, AuthorAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(Article, ArticleAdmin)

