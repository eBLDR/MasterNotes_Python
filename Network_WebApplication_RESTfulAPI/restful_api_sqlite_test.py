#!/usr/bin/python3
"""
Run from terminal

restful_api_requests_test.py <url> - will run the test script on the API found in the <url>.

Do NOT ADD slash at the end of the url.
"""
import sys

import requests


def script_usage():
    # Program's usage
    print('Usage:\n\trestful_api_requests_test.py <url> -'
          ' will run the test script on the API found in the <url>.')


def display_event(method, success, res):
    msg = 'OK' if success else 'FAILED'
    if success:
        text = res.text if str(res.status_code) == '200' else 'Database error.'
        print('{} request {}, at url: {}, status: {}, response: {}'.format(method, msg, res.url, res.status_code, text))
    else:
        print('{} request {}, error: {}'.format(method, msg, res))


def request_get(url, id_=None):
    try:
        payload = {'id': id_} if id_ else {}
        response = requests.get(url, params=payload)
        display_event('GET', 1, response)

    except Exception as e:
        display_event('GET', 0, e)


def request_post(url):
    try:
        payload = {
            'title': 'CREATE_TEST',
            'year': '1000',
        }
        response = requests.post(url, json=payload)
        display_event('POST', 1, response)

    except Exception as e:
        display_event('POST', 0, e)


def request_put(url, id_):
    try:
        payload = {
            'id': id_,
            'title': 'UPDATE_TEST',
            'year': '1500',
        }
        response = requests.put(url, json=payload)
        display_event('PUT', 1, response)

    except Exception as e:
        display_event('PUT', 0, e)


def request_delete(url, id_):
    try:
        payload = {'id': id_}
        response = requests.delete(url, params=payload)

        display_event('DELETE', 1, response)

    except Exception as e:
        display_event('DELETE', 0, e)


def input_method():
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    while True:
        method = input(str(methods) + ' (or QUIT): ').upper()
        if method in methods:
            return method
        elif method == 'QUIT':
            sys.exit()


def input_id(all_=False):
    prompt = 'Id: ' if not all_ else 'Id (or all): '
    while True:
        id_ = input(prompt)
        if id_.isdigit() or (id_.upper() == 'ALL' and all_):
            return int(id_) if id_.isdigit() else None


def run_test(url):
    print('\nThis script tests the HTTP requests from client to server. \
    Exceptions (if any) raised during execution is due to missing records in database.')

    while True:
        method = input_method()

        if method == 'GET':
            id_ = input_id(all_=True)
            request_get(url, id_)

        elif method == 'POST':
            request_post(url)

        elif method == 'PUT':
            id_ = input_id()
            request_put(url, id_)

        elif method == 'DELETE':
            id_ = input_id()
            request_delete(url, id_)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        URL = sys.argv[1]

    else:
        script_usage()
        sys.exit(1)

    if URL:
        run_test(URL)
