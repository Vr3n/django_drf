from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test_view(request):
    data = {
        'name': 'Viren',
        'age': 20
    }

    return JsonResponse(data, safe=False) # safe = false - is used to parse in Data types other than disctionary like - lists.