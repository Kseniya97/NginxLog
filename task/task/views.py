from rest_framework import generics, filters
from parser.models import LogModel
from .serializers import LogSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LogList(generics.ListAPIView):
    serializer_class = LogSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['http_method', 'code_answer', 'ip_adress']
    filterset_fields = ['http_method', 'code_answer']


    def get_queryset(self):
        return LogModel.objects.select_related().all()

