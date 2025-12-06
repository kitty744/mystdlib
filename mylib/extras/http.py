import urllib.request as _request
import urllib.parse as _parse
import json as _json

def get(url):
    with _request.urlopen(url) as response:
        return response.read().decode('utf-8')

def post(url, data):
    encoded_data = _parse.urlencode(data).encode('utf-8')

    with _request.urlopen(url, data=encoded_data) as response:
        return response.read().decode('utf-8')

def json_get(url):
    return _json.loads(get(url))