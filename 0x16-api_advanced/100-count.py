#!/usr/bin/python3
"""100-count module"""
import re
import requests


def count_words(subreddit, word_list, after=None):
    """
    count how many tumes a word appears in a hot posts title
    """
    user_agent = "100-count_words"
    counts = {}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"
    full_url = url.format(subreddit, after)
    headers = {"User-Agent": user_agent}
    word_list.sort()
    for word in word_list:
        counts[word] = 0
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
                    title = post["data"]["title"].lower()
                    for word in word_list:
                        if re.search(rf'\b{word}\b', title):
                            counts[word] += 1
                if "after" in dt["data"] and dt["data"]["after"] is not None:
                    count_words(
                                    subreddit,
                                    word_list,
                                    dt["data"]["after"]
                                    )
                else:
                    for word, count in counts.items():
                        if count > 0:
                            print("{}: {}".format(word, count))
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None
