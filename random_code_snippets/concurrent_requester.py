from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time
import requests


def do_request(i: int) -> None:
    start = time()
    r = requests.get('https://google.com/robots.txt')
    print(f'did request {i} (response length: {len(r.text)}) {time() - start:.5f}s\n', end='')


if __name__ == '__main__':
    NUM_REQUESTS = 5_000
    NUM_WORKERS = 10
    executor = ThreadPoolExecutor(max_workers=NUM_WORKERS)
    for i in range(NUM_REQUESTS):
        executor.submit(do_request, i)
    executor.shutdown()
    print('done')
