import django_virtual_models as v
from core.models import User, Video, Category
from django.db.models import Count
class VirtualVideo(v.VirtualModel):
    class Meta:
        model = Video
class VirtualUser(v.VirtualModel):
    videos = VirtualVideo(manager=Video.objects)
    
    amount_videos = v.Annotation(
        lambda qs, **kwargs: qs.annotate(
            amount_videos=Count("videos")
        ).distinct()
    )
    class Meta:
        model = User

class VirtualCategory(v.VirtualModel):
    videos = VirtualVideo(manager=Video.objects)
    
    class Meta:
        model = Category
