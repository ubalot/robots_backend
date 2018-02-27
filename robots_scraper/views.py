from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from robots_scraper.models import WebSite


@csrf_exempt
def website(request):
    """ Accept a POST request with website and robots urls.

    :param request: WSGIRequest
    :return: HttpResponse
    """
    if request.method == 'POST':
        domain = request.POST.get('domain')
        website_url = request.POST.get('website')
        robots_url = request.POST.get('robots')

        _website = WebSite(domain=domain, url=website_url, robots_url=robots_url)
        _website.save()

        # return HttpResponse(json.dumps({
        return JsonResponse({
            'success': 1,
            'data': {
                'website_url': website_url,
                'robots_url': robots_url
            }
        })  #)
    else:
        return JsonResponse({
            'success': 0,
            'message': 'Do a POST request.'
        })


@csrf_exempt
def test(request):
    return JsonResponse({
        'success': 1
    })