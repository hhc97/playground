import threading

import requests


def get_stuff(name: str):
    for i in range(20):
        r = requests.get('https://spatial-logs.herokuapp.com/test/refresh')
        print(f'thread {name} did request {i}')
        with open('logs.txt', 'a') as f:
            f.write(r.text)


if __name__ == '__main__':
    threads = []
    for t in range(6):
        thread = threading.Thread(target=get_stuff, args=(t,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print('main thread done')
