from .imports import *


@api_view(['GET'])
def list_article():
    articles = Article.objects.all()
    context = {'server': 'http://127.0.0.1:8000'}
    serializer = ArticleSerializer(articles, many=True, context=context)
    return Response(serializer.data, status=HTTP_200_OK)
