import requests
import sys
from clint.textui import progress
from datetime import datetime
import os

def download_file(url, file_name):
    r = requests.get(url, stream=True)
    last_modfied = None
    with open(file_name, 'wb') as f:
        print(r.headers)
        last_modfied = r.headers['Last-Modified']
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
    return last_modfied


url = 'https://thing-72-game.s3.amazonaws.com/game.zip'
file_name = "game.zip"

download_date = download_file(url, file_name)
print(download_date)
local_date = os.path.getmtime(file_name)
local_date = datetime.fromtimestamp(local_date).strftime('%Y-%m-%d %H:%M:%S')
print(local_date)

print('hi')