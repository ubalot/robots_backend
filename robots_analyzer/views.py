import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@api_view(['GET'])
@csrf_exempt
def content(request):
    """ Return robots.txt content for given url

    :param request: Request
    :return: json
    """
    url = request.GET.get('url')
    if not url:
        return JsonResponse({
            'success': 0,
            'message': 'Wrong argument: use "url" as argument name.'
        })

    try:
        response = requests.get(url)
    except Exception as err:
        return JsonResponse({
            'success': 0,
            'message': 'Invalid or broken url.'
        })

    if not response:
        return JsonResponse({
            'success': 0,
            'message': 'Wrong url. Retry with a correct one.'
        })

    robots_txt = response.content.decode('utf-8')
    return JsonResponse({
        'success': 1,
        'data': robots_txt
    })


@api_view(['GET'])
@csrf_exempt
def test(_, __):
    return JsonResponse({
        'success': 1
    })