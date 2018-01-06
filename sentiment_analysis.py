# -*- coding: utf-8 -*-

import http.client, urllib
import json

accessKey = "07e47a6d41ed4ad78737e98b403e0d68"

# import socket
# import socks

# socks.set_default_proxy(socks.SOCKS5, "proxy22.iitd.ac.in", 3128)
# socket.socket = socks.socksocket
import requests

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    body = json.dumps (documents)
    # conn.request ("POST", path, body, headers)
    # response = conn.getresponse ()
    data = requests.post("https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/semtiment", headers = headers, data = body, verify=False)
    return data.text

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' },
    { 'id': '2', 'language': 'es', 'text': 'Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico.' }
]}

print('Please wait a moment for the results to appear.\n')

result = GetSentiment (documents)
print (json.dumps(json.loads(result), indent=4))