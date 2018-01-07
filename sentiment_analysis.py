# -*- coding: utf-8 -*-

# import http.client, urllib
import json
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
# accessKey = "07e47a6d41ed4ad78737e98b403e0d68"

# SUBSCRIPTIONKEY = 
LOCATION = "southcentralus"
URL = LOCATION + ".api.cognitive.microsoft.com"
apikey='dd955a5dc6104d8596a40362503f8d56'
# import socket
# import socks

# socks.set_default_proxy(socks.SOCKS5, "proxy22.iitd.ac.in", 3128)
# socket.socket = socks.socksocket
import requests


def GetSentiment(documents):
    '''Gets the sentiments for a set of documents and returns the information.'''
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': apikey,
    }
    # headers = {'Ocp-Apim-Subscription-Key': accessKey}
    body = json.dumps(documents)
    # conn.request ("POST", path, body, headers)
    # response = conn.getresponse ()

    params = urllib.parse.urlencode({ })

    try:
        conn = http.client.HTTPSConnection(URL)
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        return data
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # return data

    # data = requests.post("https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/semtiment", headers = headers, data = body, verify=False)
    # return data.text

documents = {	
		'documents': [
    {'id': '1', 'language': 'en',
        'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.'},
    {'id': '2', 'language': 'es',
        'text': 'Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico.'}
]}

# documents = '{                                           \
#             "documents": [                          \
#                 {                                   \
#                     "language": "en",               \
#                     "id": "1",                      \
#                     "text": "I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.\
#                 },                                  \
#             ]                                       \
#         }'                                          \



print('Please wait a moment for the results to appear.\n')

result = GetSentiment(documents)
# print("result :: ")
# print(result)
print(json.dumps(json.loads(result), indent=4))
