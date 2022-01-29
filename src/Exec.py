"""
Execute File
 
@author: tatsukoni
"""

import infrastructure.ApiCall as ApiCall

api_key = 'YOUR API KEY'
api_secret = 'YOUR API SECRET KEY'
api_endpoint = 'ACCESS ENDPOINT'

if __name__ == '__main__':
    api = ApiCall.ApiCall(api_key, api_secret, api_endpoint)

    # public GET Usage
    # path = '/v/public'
    # res = api.get_public(path)
    # print(res)

    # private GET Usage
    # path = '/v/private'
    # res = api.get_private(path)
    # print(res)

    # private POST Usage
    # path = '/v/private'
    # params = {
    #     "key1": "hoge",
    #     "key2": "hogehoge",
    #     "key3": 12345
    # }
    # res = api.post_private(path, params)
    # print(res)
