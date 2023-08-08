#!/usr/bin/python3
"""2-recurse module"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    use:
        create a list of 10 hot articles for a given
        subreddit
    args:
        subredddit - subreddit to query
        hot_list - list of hot articles
        after - set item per list
    return:
        list of hot articles or None
    """

    user_agent = "2-recurse"
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"
    full_url = url.format(subreddit, after)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(
                                full_url,
                                headers=headers,
                                allow_redirects=False
                                )
        if response.status_code == 200:
            dt = response.json()
            if "data" in dt and "children" in dt["data"]:
                posts = dt["data"]["children"]
                for post in posts:
                    hot_list.append(post["data"]["title"])
                if "after" in dt["data"] and dt["data"]["after"] is not None:
                    recurse(subreddit, hot_list, dt["data"]["after"])
                return hot_list
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None
