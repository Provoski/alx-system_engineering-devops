#!/usr/bin/python3
"""100-count module"""
import re
import requests


def count_words(subreddit, word_list, after=None):
    user_agent = "100-count_words"
    counts = {}
    print(counts)
    sorted__word_list = sorted(word_list)
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"
    full_url = url.format(subreddit, after)
    headers = {"User-Agent": user_agent}
    for word in sorted_word_list:
        counts[word] = 0
    try:
        response = requests.get(full_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and "children" in data["data"]:
                posts = data["data"]["children"]
                for post in posts:
                    title = post["data"]["title"].lower()
                    for word in sorted_word_list:
                        if re.search(r'\b' + word + r'\b', title):
                            counts[word] += 1
                if "after" in data["data"] and data["data"]["after"] is not None:
                    return count_words(subreddit, word_list, data["data"]["after"])
                else:
                    for word, count in counts.items:
                        if count > 0:
                            print("{}: {}".format(word, count))
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None
