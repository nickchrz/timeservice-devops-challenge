#!/usr/bin/env python3
""" Health check script for timeservice website """

import re
import requests
import argparse
import validators
import datetime
import time

def health_check(url):
    page = requests.get(url)
    response = 'OK'
    if not page.status_code == 200:
        response = f'ALERT: Invalid response from url: {url}'
    else:
        timeservice = page.text
        try:
            service_timestamp = time.mktime(datetime.datetime.strptime(timeservice, "%Y-%m-%d %H:%M:%S %z").timetuple())
            now = time.time()
            # ditch the miliseconds
            service_sec = str(service_timestamp).split('.')[0]
            now_sec = str(now).split('.')[0]
            if not now_sec == service_sec:
                response = "ALERT: Timeservice is not in sync"
        except Exception:
            response = f'ALERT: Unable to parse timestamp: {timeservice}'
    return response

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--debug',
        action = 'store_true',
        help = 'print additional logging')
    parser.add_argument('--url',
        nargs = '?',
        default = 'http://timeservice01-elb-1646580280.eu-west-2.elb.amazonaws.com/now',
        help = 'url of timeservice application')
    args = parser.parse_args()
    if not validators.url(args.url):
        print(f'{args.url} is not a valid URL')
    result = health_check(args.url)
    print(result)

if __name__ == '__main__':
    main()