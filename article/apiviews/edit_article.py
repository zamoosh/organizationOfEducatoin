from .imports import *


class EditArticle(RetrieveUpdateDestroyAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.article = None

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['pk'])
        self.article = article
        context = {'request': request}
        return Response(ArticleSerializer(article, context=context).data, status=HTTP_200_OK)

    def get_view_name(self):
        if hasattr(self.article, 'name'):
            return self.article.name
        else:
            return super(EditArticle, self).get_view_name()

    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]
