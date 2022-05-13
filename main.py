import json
import requests
import time

TOKEN = input("User Account Token ~")
CHANNEL = input("Channel ID ~")



def fetch(lastid, limit, channel):
    if lastid == None:
        request = f"https://discord.com/api/v9/channels/{channel}/messages?limit={limit}"
    else:
        request = f"https://discord.com/api/v9/channels/{channel}/messages?before={lastid}&limit={limit}"
    re = requests.get(request, headers={
        "x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA0Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTI4MDMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "authorization":TOKEN,
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9004 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
        "x-debug-options":"bugReporterEnabled",
        "x-discord-locale":"en-US",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode":"cors",
        "sec-fetch-dest":"empty",
        "accept-language":"en-US,en-CA;q=0.9",
        "accept-encoding":"gzip, deflate, br",
        "accept":"*/*"
    })
    print(f"FETCHED: {re.status_code}")
    return json.loads(re.text)

def addall(messagno):
    for item in messagno:
        outlog.append(item)
        print("POP -> " + item['content'])

outlog = []


print("Connecting to discord...")
lastfetch = fetch(None, 50, CHANNEL)
lastsize = len(lastfetch)
addall(lastfetch)

while lastsize > 49:
    lastfetch = fetch(lastfetch[len(lastfetch) - 1]['id'], 50, CHANNEL)
    addall(lastfetch)
    lastsize = len(lastfetch)
    time.sleep(0.5)

with open(f"log-{CHANNEL}.json", "w+") as file:
    file.write(json.dumps({"messages":outlog}))

print("Done downloading chat!")
input()

