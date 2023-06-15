from django.shortcuts import render
from articles.models import Article
# Create your views here.


def article_search_view(request):
    try: 
        query_id = int(request.GET.get('q'))
    except:
        query_id = None

    obj = None
    if query_id is not None and query_id is not '':
        obj = Article.objects.get(id=int(query_id))

    context = {
        'object': obj,
    }
    return render(request, "articles/search.html", context=context)

def article_create_view(request):
     
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title is not None and title is not '': 
            Article.objects.create(title=title, content=content)
        

    context={
         
    }
    return render(request, 'articles/create.html', context=context)

def article_detail_view(request, id=None):
    obj = None
    if id is not None:
        obj = Article.objects.get(id=id)
    context = {
        "object": obj,
    }
    return render(request, "articles/details.html", context=context)
