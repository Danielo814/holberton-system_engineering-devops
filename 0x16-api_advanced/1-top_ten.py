#!/usr/bin/python3
"""
1-top_ten module
"""


def top_ten(subreddit):
    """
    top 10 subreddit titles
    """
    import requests
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    response = requests.get('https://www.reddit.com/r/{}/top/.json'.
                            format(subreddit),
                            headers={'User-Agent': 'Daniel:Api:Project'})
    try:
        response_dict = response.json()
        new_list = response_dict['data']['children']
        index = 0
        while (index < 10):
            print(new_list[index]['data']['title'])
            index = index + 1
    except:
        print(None)
        return
