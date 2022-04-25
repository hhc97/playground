import threading
from time import time

import requests


def do_request(name: str):
    for i in range(20):
        start = time()
        r = requests.get('https://google.com/robots.txt')
        print(f'thread {name} did request {i} (response length: {len(r.text)}) {time() - start:.5f}s\n', end='')


if __name__ == '__main__':
    threads = []
    for t in range(8):
        thread = threading.Thread(target=do_request, args=(t,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print('main thread done')
