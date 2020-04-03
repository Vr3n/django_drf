from django.urls import path
from core.views import *
# Write your url patterns here.

urlpatterns = [
    path('', TestView.as_view(), name='test'),
]
