#!/usr/bin/python3
"""
Python script
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints posts"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("[{}] {}".format(r.status_code, r.text))
    posts = r.json()
    for data in posts:
        print(data["title"])

def fetch_and_save_posts():
    """Fetches and saves posts"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        data = [{'id': new['id'], 'title': new['title'],
                'body': new['body']} for new in post]
        with open('posts.csv', 'w') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
