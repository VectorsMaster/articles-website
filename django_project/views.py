from django.http import HttpResponse


from articles.models import Article
from django.template.loader import render_to_string
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    obj = Article.objects.get(id=2)
    

    my_list = Article.objects.all()

    context = {
        'my_list': my_list,
        'title': obj.title,
        'id': obj.id,
        'content': obj.content
    }
    
    response = render_to_string('home_view.html', context=context)
    return HttpResponse(response)
    