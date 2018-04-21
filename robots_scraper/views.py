import re
import requests
import urllib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from robots_scraper.models import WebSite


@csrf_exempt
def add_website(request, id=None):
    """ Accept a POST request with robots.txt url as parameter.

    :param request: WSGIRequest
    :return: JsonResponse
    """
    if request.method == 'GET':
        url = request.GET.get('url', None)
        if not url:
            return JsonResponse({
                'success': 0,
                'message': 'A parameter named "url" is needed.'
            })

        WebSite.websites.filter(url=url)

    elif request.method == 'POST':
        url = request.POST.get('url', None)
        if not url:  # wrong parameter name
            return JsonResponse({
                'success': 0,
                'message': 'A parameter named "url" is needed.'
            })

        try:
            requests.get(url)
        except Exception:
            return JsonResponse({
                'success': 0,
                'message': "website '{}' doesn't exists. It hasn't been added into the database.".format(url)
            })

        if not re.match(r'^http(s)?://', url, re.IGNORECASE):
            url = 'http://' + url

        parsed = urllib.parse.urlparse(url)

        website_url = parsed.netloc
        domain = re.sub(r'^www\.', '', website_url)

        # Add website to db only if it isn't already in it.
        if WebSite.websites.filter(domain=domain):
            return JsonResponse({
                'success': 0,
                'message': 'website with domain "{}" already exists.'.format(domain)
            })

        website = WebSite(domain=domain, url=website_url, robots_url=url)
        website.save()

        return JsonResponse({
            'success': 1,
            'data': {
                'website': website_url,
                'domain': domain,
                'robots_url': url
            }
        })

    elif request.method == 'DELETE':
        if id is None:
            return JsonResponse({
                'success': 0,
                'message': 'DELETE request needs a id in order to delete a website from database.'
            })
        tot_deleted_items, deleted_items = WebSite.websites.filter(id=id).delete()
        return JsonResponse({
            'success': 1,
            'data': {
                'tot_deleted_items': tot_deleted_items,
                'deleted_items': deleted_items
            }
        })

    return JsonResponse({
        'success': 0,
        'message': 'Do a POST request.'
    })


@csrf_exempt
def websites_list(request):
    """ Accept GET request and return all websites in the db.

    :param request: WSGIRequest
    :return: JsonResponse
    """
    if request.method != 'GET':
        return JsonResponse({
            'success': 0,
            'message': 'Do a GET request'
        })

    websites = WebSite.websites.all()

    result = [{
        'domain': w.domain,
        'url': w.url,
        'robots_url': w.robots_url
    } for w in websites]

    return JsonResponse({
        'success': 1,
        'data': {
            'websites': result
        }
    })


@csrf_exempt
def test(request):
    """ Simple API for testing purpose only. It accepts every type of request; return a generic Json to show that
    it's alive.

    :param request: WSGIRequest
    :return: JsonResponse
    """
    return JsonResponse({
        'success': 1
    })