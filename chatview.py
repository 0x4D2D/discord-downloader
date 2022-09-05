import json

file = input("File to Load~")
write = input("File to write parsed output to? (leave blank for none) ~")

buf = "--START OF CHAT LOGS--\n"

with open(file, "r") as handle:
    obj = json.loads(handle.read())
    messages = obj['messages']
    for message in messages:
        buf = buf + f"{message['author']['username']}: {message['content']}\n"
        print(f"{message['author']['username']}: {message['content']}")

buf = buf + "--END OF CHAT LOGS--\n"

if len(write) > 0:
    with open(write, "w+", encoding='utf-8') as handle:
        handle.write(buf)

input()
