import collections

import requests


def get_robots_txt(url):
    """
    :param url: str
    :return: str | None
    """

    if not url.endswith('robots.txt'):
        url += 'robots.txt' if url[-1] == '/' else '/robots.txt'

    response = requests.get(url)

    if response:
        return response.text

    return None


def robots_extrapolation(text):
    """Return dictionary with lists as values.
    :param text: str
    :return: collections.defaultdict | None
    """
    if not text:
        return None

    lines = text.splitlines()
    user_agents = {}
    user_agent = None
    for line in lines:
        if line and line[0] != '#':  # avoid empty lines and  line comments
            key, value = line.split(':', maxsplit=1)  # split at first ':'
            cleared_value = value.split(' #', maxsplit=1)[0].strip()  # avoid comments
            if key == 'User-agent':
                user_agent = cleared_value
                user_agents[user_agent] = collections.defaultdict(list)
            else:
                user_agents[user_agent][key].append(cleared_value)
    return user_agents
