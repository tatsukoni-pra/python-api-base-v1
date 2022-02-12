"""
Execute File
 
@author: tatsukoni
"""

import os
from dotenv import load_dotenv
import infrastructure.ApiCall as ApiCall
import infrastructure.RealtimeApiCall as RealtimeApiCall

class RuntimeContext:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.api_endpoint = os.getenv("API_ENDPOINT")
        self.realtime_api_endpoint = os.getenv("REALTIME_API_ENDPOINT")
        self.realtime_api_channel = os.getenv("REALTIME_API_CHANNEL")

if __name__ == '__main__':
    runtimeContext = RuntimeContext()

    # API Usage
    # api = ApiCall.ApiCall(api_key, api_secret, api_endpoint)

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

    # RealTime API Usage
    realtimeApi = RealtimeApiCall.RealtimeApiCall(
        url=runtimeContext.realtime_api_endpoint,
        channel=runtimeContext.realtime_api_channel
    )
    realtimeApi.run()
