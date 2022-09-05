import json

file = input("File to Load~")
write = input("File to write parsed output to? (leave blank for none) ~")

buf = ""

with open(file, "r") as handle:
    obj = json.loads(handle.read())
    messages = obj['messages']
    for message in messages:
        buf += f"{message['author']['username']}: {message['content']}\n"
        print(f"{message['author']['username']}: {message['content']}")

if len(write) > 0:
    with open(write, "w+") as handle:
        handle.write(buf)
