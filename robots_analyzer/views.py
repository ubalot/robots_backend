import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def content(request):
    """ Return robots.txt content for given url

    :param request: <url>
    :return: json
    """
    if request.method == 'GET':
        url = request.GET.get('url')
        if url:
            response = requests.get(url)
            if response:
                robots_txt = response.content.decode('utf-8')

                return JsonResponse({
                    'success': 1,
                    'data': robots_txt
                })

            return JsonResponse({
                'success': 0,
                'message': 'Wrong url. Retry with a correct one.'
            })

        return JsonResponse({
            'success': 0,
            'message': 'Wrong argument: use "url" as argument name.'
        })

    return JsonResponse({
        'success': 0,
        'message': 'Do a GET request.'
    })


@csrf_exempt
def test(request):
    return JsonResponse({
        'success': 1
    })