from .imports import *


class EditArticle(RetrieveUpdateDestroyAPIView):
    def __init__(self, **kwargs):
        self.article = None
        if 'pk' in kwargs:
            self.article = None
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs['pk'])
        self.article = article
        context = {'server': 'http://127.0.0.1:8000'}
        serializer = ArticleSerializer(article, context=context)
        return Response(serializer.data, status=HTTP_200_OK)

    def get_serializer_class(self):
        return ArticleSerializer

    def get_serializer_context(self):
        return {'server': 'http://127.0.0.1:8000'}

    def get_view_name(self):
        if hasattr(self.article, 'name'):
            return self.article.name
        else:
            return super(EditArticle, self).get_view_name()

    def get_view_description(self, html=False):
        return 'kir'
