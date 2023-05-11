#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit
    API and returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": ",mclovin-bot/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("Subreddit '{}' not found".format(subreddit))
        else:
            print("An HTTP error occured: {}".format(e))
        return 0
    except requests.exceptions.RequestException as e:
        print("A network error occured: {}".format(e))
        return 0

    data = response.json()
    return data.get('data').get('subscribers')
