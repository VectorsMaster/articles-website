from django.contrib import admin

# Register your models here.


from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Article, ArticleAdmin)
