from .imports import *


@api_view(['GET'])
def list_article_student(request):
    if request.method == 'GET':
        context = {'server': 'http://127.0.0.1:8000'}
        articles = Article.objects.filter(is_master=False)
        serializer = ArticleSerializer(articles, many=True, context=context)
        return Response(serializer.data, status=HTTP_200_OK)
