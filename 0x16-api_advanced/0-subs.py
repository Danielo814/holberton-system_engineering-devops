#!/usr/bin/python3
"""
0-subs module
"""


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    import requests
    if subreddit is None or type(subreddit) is not str:
        return 0
    response = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit),
                            headers={'User-Agent': 'Daniel:Api:Project'})
    if response.status_code != 200:
        return 0
    response_dict = response.json()
    return response_dict['data']['subscribers']
