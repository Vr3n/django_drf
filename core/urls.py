from django.urls import path
from core.views import *
# Write your url patterns here.

urlpatterns = [
    path('', PostView.as_view(), name='test'),
    path('api/create/', PostCreateView.as_view(), name='post-create'),
    path('api/list_create/', PostListCreateAPIView.as_view(), name='post-lc'),
]
