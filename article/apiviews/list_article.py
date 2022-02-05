from .imports import *


class ListArticle(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
