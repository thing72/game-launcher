import requests
import sys
from clint.textui import progress
from datetime import datetime
import os
import zipfile
import shutil

def download_file(url, file_name):
    r = requests.get(url, stream=True)
    last_modfied = None
    with open(file_name, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()


url = 'https://thing-72-game.s3.amazonaws.com/game.zip'
file_name = "game.zip"


download_file(url,file_name)

try:
    shutil.rmtree("unzip")
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

# unzip the file
try:
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall("unzip")
except:
    print("folder already there")

# exec the file
os.startfile("unzip\myapp.exe")

print('hi')