from rest_framework.generics import ListAPIView
from core.serializers import UserSerializer, CategorySerializer
from core.models import User, Category
from django.db import connection, reset_queries
import django_virtual_models as dvm



# class UserListAPIView(ListAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         users = User.objects.prefetch_related("videos")
#         for query in connection.queries:
#             print("Query:", query)
        
#         reset_queries()
        
#         return users


class UserListAPIView(dvm.VirtualModelListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):

        queryset = super().get_queryset()
        for query in connection.queries:
            print("Query:", query)
        reset_queries()
        return queryset

class CategoriesListAPIView(dvm.VirtualModelListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):

        queryset = super().get_queryset()
        for query in connection.queries:
            print("Query:", query)
        reset_queries()
        return queryset
    
    

