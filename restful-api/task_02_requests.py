#!/usr/bin/python3
"""
Python script
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints posts"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        post = r.json()
        for data in post:
            print(data["title"])


def fetch_and_save_posts():
    """Fetches and saves posts"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        post = r.json()
        data = [{'id': new['id'], 'title': new['title'],
                'body': new['body']} for new in post]
        with open('posts.csv', 'w') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
