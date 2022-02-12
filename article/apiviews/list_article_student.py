from .imports import *


class ListArticleStudent(ListAPIView):
    queryset = Article.objects.not_master()
    serializer_class = ArticleSerializer
