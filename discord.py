import requests
import os
import time
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)
os.system("cls" or "clear")

with open("token.txt") as f:
    token = f.read()
    
with open("content.txt") as f:
    content = f.read()

channel = "https://discord.com/api/v9/channels/1/messages"
channel = channel[:36] + input(Fore.LIGHTYELLOW_EX + "Channel ID?: ") + "/messages"
speed = float(input(Fore.LIGHTGREEN_EX + "How fast should the messages send (in seconds): "))
repeat = int(input(Fore.LIGHTRED_EX + "How many times do you wanna send the message: "))
ratelimit = int(input(Fore.LIGHTBLUE_EX + "When you get ratelimited, how long do you want to wait for messages to be sent again: "))

os.system('cls')

header = {
    'authorization': token
}

payload = {
    'content': content
}

for i in range (repeat):
    time.sleep(speed)

    r = requests.post(channel, json=payload, headers=header)
    if r.status_code == requests.codes.ok:
        print(Fore.GREEN + "Message sent!")
    else:
        print(Fore.RED + "You are being ratelimited!")
        time.sleep(ratelimit)
