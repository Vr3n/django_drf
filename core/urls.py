from django.urls import path
from core.views import test_view
# Write your url patterns here.

urlpatterns = [
    path('', test_view, name='test')
]
