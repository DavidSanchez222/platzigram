"""platzigram views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def hello_word(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Curren server time is {now}')


def sorted(request):
    """Return a JSON response with sorted integers."""
    # import pdb; pdb.set_trace()
    # numbers = map(lambda x: int(x), request.GET['numbers'].split(','))
    numbers = map(int, request.GET['numbers'].split(','))
    numbers = sorted(numbers)
    context = {
        'numbers': numbers
    }
    return JsonResponse(context, json_dumps_params={'indent': 4})


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f'Sorry {name}, you are not allowed here.'
    else:
        message = f'Hello, {name}! Welcome to Platzigram.'
    return HttpResponse(message)
