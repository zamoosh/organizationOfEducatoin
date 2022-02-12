from .imports import *


@api_view(['GET'])
def list_article_master(request):
    if request.method == 'GET':
        context = {'server': 'http://127.0.0.1:8000'}
        articles = Article.objects.filter(is_master=True)
        articles_serializer = ArticleSerializer(articles, many=True, context=context)
        return Response(articles_serializer.data, status=HTTP_200_OK)
