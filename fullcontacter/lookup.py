'''
Fullcontacter: A wrapper for the excellent and helpful Fullcontact.com APIs
Fullcontacter version 0.3

Utility module that uses requests to do the heavy lifting and get the data for further handling

'''


import requests

#configuration
API_VERSION = 'v2'
END_POINT = 'https://api.fullcontact.com/{0}/'.format(API_VERSION)

CLIENT_VERSION = '0.3'
USER_AGENT = 'Python /Fullcontacter: Fullcontact wrapper for Python. version {0} http://pypi.python.org/pypi/fullcontacter'.format(CLIENT_VERSION)


def lookup_request(fc_api, format, api_key, **kwargs):
    lookup_end_point = END_POINT + fc_api + format

    payload = {}
    for key, value in kwargs.items():
        payload[key] = value
    payload['apiKey'] = api_key

    lookup_request = requests.get(lookup_end_point, headers={'User-Agent': USER_AGENT}, params=payload)

    if format == '.json':
        results = {'satus_code': lookup_request.status_code, 'url': lookup_request.url, 'lookup': lookup_request.json()}
    else:
        results = {'satus_code': lookup_request.status_code, 'url': lookup_request.url, 'lookup': lookup_request.text}

    return results
