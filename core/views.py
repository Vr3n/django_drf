from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

# def test_view(request):
#     data = {
#         'name': 'Viren',
#         'age': 20
#     }

#     return JsonResponse(data, safe=False) # safe = false - is used to parse in Data types other than disctionary like - lists.

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Viren',
            'age': 20
        }
        return Response(data)