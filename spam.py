# Imports

import requests
import time
import os
from threading import Thread

# Files it will read from

with open("token.txt", "r") as f:
    token = f.read()

with open("content.txt", "r") as f:
    content = f.read()

with open("channel.txt", "r") as f:
    channel = f.read()

    



# Payload's And Headers.

payload = {
    'content': content
}

header = {
    'authorization': token
}

# The loop itself

for i in range (1000000000000000000000000):
    time.sleep(2)

    r = requests.post(channel, json=payload, headers = header)

    print("Message Sent!")


