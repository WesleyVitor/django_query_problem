from rest_framework import serializers
from core.models import User, Video, Category
import django_virtual_models as dvm
from core.virtual_models import VirtualUser, VirtualCategory
from django.db.models import Count
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ("title","url","visualizations")
# class UserSerializer(serializers.ModelSerializer):
#     videos = VideoSerializer(many=True)
#     amount_videos = serializers.SerializerMethodField()
#     class Meta:
#         model = User
#         fields = ("name", "videos", "amount_videos")

#     def get_amount_videos(self, obj):
#         return Video.objects.filter(user=obj).count()

class UserSerializer(dvm.VirtualModelSerializer):
    videos = VideoSerializer(many=True)
    amount_videos = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = User
        virtual_model = VirtualUser
        fields = ("name", "videos","amount_videos")
    
class CategorySerializer(dvm.VirtualModelSerializer):
    videos = VideoSerializer(many=True)
    
    
    class Meta:
        model = Category
        virtual_model = VirtualCategory
        fields = ("title","videos")

# class CategorySerializer(serializers.ModelSerializer):
#     videos = VideoSerializer(many=True)

#     class Meta:
#         model = Video
#         fields = ("title")
    