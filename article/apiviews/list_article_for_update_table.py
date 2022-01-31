from .imports import *


class ListArticleForUpdateTable(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
