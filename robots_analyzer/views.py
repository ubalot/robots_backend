import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def content(request):
    """ Return robots.txt content for given url

    :param request: Request
    :return: json
    """
    if request.method != 'GET':
        return JsonResponse({
            'success': 0,
            'message': 'Do a GET request.'
        })

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
            'message': 'Invalid url.\nError: {}'.format(err)
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


@csrf_exempt
def test(request, name):
    return JsonResponse({
        'success': 1
    })