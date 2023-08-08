#!/usr/bin/python3
""""0-subs module"""
import requests


def number_of_subscribers(subreddit):
    """
    args:
        subreddit - variable for subreddit to querry
    return:
        returns number of subscribers for a given subreddit
        or 0 if invalid subreddit is given
    """

    user_agent = "0-subs"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "subscribers" in data["data"]:
                return data["data"]["subscribers"]
            else:
                return 0
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
