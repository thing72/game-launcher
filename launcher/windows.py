import requests
import sys
from clint.textui import progress

# def download_file(link, file_name):
#     with open(file_name, "wb") as f:
#         print("Downloading %s" % file_name)
#         response = requests.get(link, stream=True)
#         total_length = response.headers.get('content-length')

#         if total_length is None: # no content length header
#             f.write(response.content)
#         else:
#             dl = 0
#             total_length = int(total_length)
#             for data in response.iter_content(chunk_size=4096):
#                 dl += len(data)
#                 f.write(data)
#                 done = int(50 * dl / total_length)
#                 sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
#                 sys.stdout.flush()
#     print()

def download_file(url, file_name):
    r = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()


url = 'https://thing-72-game.s3.amazonaws.com/game.zip'
file_name = "game.zip"

download_file(url, file_name)

print('hi')