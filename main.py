import os
import urllib.request as req
import urllib.error
import random
import json
import tempfile
import sys


if len(sys.argv) < 2:
    funny = 10
else:
    funny = int(sys.argv[1])

funnylinks = []
funnynames =[]
after = None
print("fetching stuff")
while True:
    try:
        with req.urlopen(f"https://api.reddit.com/r/Animewallpaper/new?after={after}") as c:
            data = json.load(c)
    except urllib.error.HTTPError as s:
        continue
    
    for i in data["data"]["children"]:
        if "url_overridden_by_dest" not in i["data"]:
            continue
        x = i["data"]["url_overridden_by_dest"]
        if "gallery" not in x and "Mobile" not in i["data"]["link_flair_text"] and i["data"]["post_hint"] == "image":
           funnylinks.append(x)
           funnynames.append(i["data"]["title"])
    after = data["data"]["after"]
    if len(funnylinks) > funny:
        break
for i,b in enumerate(funnynames):
    print(i+1 , " - " , b , f"{funnylinks[i]}")
z = input("choose one(or type \"random\"): ")
if z == "random":
    z = random.randint(1, len(funnylinks[i]))
with req.urlopen(funnylinks[int(z)-1]) as img:
    with tempfile.NamedTemporaryFile("w+b", delete=False, suffix="." + x.split(".")[-1]) as file:
        file.write(img.read())
        os.system(f"feh --bg-scale {file.name}")
        print("i weebafied you mf")
