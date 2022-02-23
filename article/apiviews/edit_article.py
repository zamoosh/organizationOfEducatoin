from .imports import *


class EditArticle(RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['pk'])
        context = {'request': request}
        return Response(ArticleSerializer(article, context=context).data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT' or request.method == 'PATCH':
            article = Article.objects.get(id=kwargs['pk'])
            article.name = request.data.get('name')
            article.title = request.data.get('title')
            article.subject = request.data.get('subject')
            article.author = request.data.get('author')
            article.description = request.data.get('description')
            article.is_confirmed = bool(request.data.get('is_confirmed'))
            article.is_master = bool(request.data.get('is_master'))
            if request.FILES:
                article.file.delete(save=False)
                article.file = request.data.get('file')
            context = {'request': request}
            article.save()
            return Response(ArticleSerializer(article, context=context).data, status=HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]
