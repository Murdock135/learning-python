
'''
Key Topic: multiprocessing
-------------------------
source: Fluent Python 2 ed.

This program uses python's [multiprocessing module] to runs a script and displays a spinner '\|/' while the program is running.

- The spin() and slow() will run concurrently


Additional info:
- By design, there is no API for terminating a thread. You must send a message to shut down.
- Python's threading.Event is the simplest signalling mechanism to coordinate threads.
'''

import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    import math
    root = math.isqrt(n)
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False
    return True

def spin(msg: str, done: synchronize.Event) -> None: # This will run in a separate thread
    i = 1
    for char in itertools.cycle(r'\|/-'): # This will yield an infinite loop because itertools.cycle() cycles infinitely
        status = f'\r{char} {msg}'
        print(i)
        print(status, end='', flush=True)

        i+=1
        if done.wait(.1): # The Event.wait(timeout=None) method returns True when the event is set by another thread; if Timeout elapses, it returns False. The .1s timeout sets the framerate of the animation to 10 FPS
            break

        blanks = ' ' * len(status)
        print(f'\r{blanks}\r')

# slow() will be called by the main thread
# This will block the main thread and release GIL, allowing other threads to run
def slow() -> int: 
    start_time = time.perf_counter()
    _ = is_prime(5000111000222021)
    elapsed_time = time.perf_counter() - start_time
    print(f'\n[Timing] is_prime took {elapsed_time:.4f} seconds')
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')

    spinner.start()
    result = slow()
    done.set()
    spinner.join()

    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
