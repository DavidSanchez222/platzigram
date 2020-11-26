"""platzigram views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def hello_word(request):
    """ """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Curren server time is {now}')


def hi(request):
    """Hi 10,4,50,32"""
    # import pdb; pdb.set_trace()
    numbers = map(lambda x: int(x), request.GET['numbers'].split(','))
    numbers = sorted(numbers)
    context = {
        'numbers': numbers
    }
    return JsonResponse(context, json_dumps_params={'indent': 4})