import os
import requests as req
from time import sleep


heads = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0"
    ),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "text/plain;charset=UTF-8",
    #   "Sec-GPC": "1",
    # "Connection": "keep-alive",
    "Referer": "https://apkpure.com/",
}


import re

for p in packs:
    print(p)
    try:
        r = req.get(f'https://apkpure.com/search?q={p}', headers=heads)
        print(r, r.status_code)
        href = re.search(
            r'(https://apkpure.com/[a-zA-Z-_.]+/[a-zA-Z-_.]+)', r.text
        )
        r = req.get(href.group(0) + '/downloading', headers=heads)
        print(r.text)

        sleep(1)
    except Exception as e:
        print(e)
