from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerialier
from .models import Post

# Create your views here.

# def test_view(request):
#     data = {
#         'name': 'Viren',
#         'age': 20
#     }

#     return JsonResponse(data, safe=False) # safe = false - is used to parse in Data types other than disctionary like - lists.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerialier(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)