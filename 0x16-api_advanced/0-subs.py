#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers of subreddit'''
import requests


def number_of_subscribers(subreddit):
    ''' get num of subs '''

    base_url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'mclovin_bot'}
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        subs_num = response.json().get('data').get('subscribers')
        return subs_num
    else:
        return 0
