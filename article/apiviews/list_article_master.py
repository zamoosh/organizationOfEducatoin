from .imports import *


@api_view(['GET'])
def list_article_master(request, format=None):
    if request.method == 'GET':
        context = {'server': 'http://127.0.0.1:8000'}
        articles = Article.objects.filter(is_master=True)
        serializer = ArticleSerializer(articles, many=True, context=context)
        return Response(serializer.data, status=HTTP_200_OK)
