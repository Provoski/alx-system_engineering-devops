#!/usr/bin/python3
""""1-top_ten module"""
import requests


def top_ten(subreddit):
    """
    use:
        first 10 hot posts listed for a given subreddit
        or print None if not a valid subreddit
    args:
        subreddit - variable for subreddit to querry
    return:
        0 on success
    """

    user_agent = "1-top_ten"
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "children" in data["data"]:
                posts = data["data"]["children"]
                for post in posts:
                    print(post["data"]["title"])
            else:
                print("None")
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
