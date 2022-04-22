import threading
from time import time

import requests


def get_stuff(name: str):
    for i in range(20):
        start = time()
        r = requests.get('https://google.com/robots.txt')
        print(f'thread {name} did request {i} (response length: {len(r.text)}) {time() - start}s')


if __name__ == '__main__':
    threads = []
    for t in range(8):
        thread = threading.Thread(target=get_stuff, args=(t,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print('main thread done')
