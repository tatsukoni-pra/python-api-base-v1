"""
API Call
 
@author: tatsukoni
"""

import json
import requests
import time
import hmac
import hashlib

class ApiCall:
    __slots__ = ['api_key', 'api_secret', 'api_endpoint']

    def __init__(self, api_key, api_secret, api_endpoint):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_endpoint = api_endpoint

    def get_public(self, path):
        return requests.get(self.api_endpoint + path).json()

    def get_private(self, path):
        timestamp = str(time.time())
        return requests.get(
            self.api_endpoint + path,
            headers = {
                'ACCESS-KEY': self.api_key,
                'ACCESS-TIMESTAMP': timestamp,
                'ACCESS-SIGN': self.__get_sign(timestamp, path),
                'Content-Type': 'application/json'
            }
        ).json()

    def post_private(self, path, params):
        payload = json.dumps(params)
        timestamp = str(time.time())
        return requests.post(
            self.api_endpoint + path,
            data = payload,
            headers = {
                'ACCESS-KEY': self.api_key,
                'ACCESS-TIMESTAMP': timestamp,
                'ACCESS-SIGN': self.__get_post_sign(timestamp, path, payload),
                'Content-Type': 'application/json'
            }
        ).json()

    def __get_sign(self, timestamp, path):
        text = timestamp + 'GET' + path
        return hmac.new(bytes(self.api_secret.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
    
    def __get_post_sign(self, timestamp, path, payload):
        text = timestamp + 'POST' + path + payload
        return hmac.new(bytes(self.api_secret.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
