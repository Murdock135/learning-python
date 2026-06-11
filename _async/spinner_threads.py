'''
This program runs a script and displays a spinner '\|/' while the program is running.

- The spin() and slow() will run concurrently
- The main thread-- The only thread when the program starts- will start a new thread to run spin() and slow()


Additional info:
- By design, there is no API for terminating a thread. You must send a message to shut down.
- Python's threading.Event is the simplest signalling mechanism to coordinate threads.
'''

import itertools
import time
from threading import Thread, Event

def spin(msg: str, done: Event) -> None: # This will run in a separate thread
    for char in itertools.cycle(r'\|/-'): # This will yield an infinite loop because itertools.cycle() cycles infinitely
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1): # The Event.wait(timeout=None) method returns True when the event is set by another thread; if Timeout elapses, it returns False. The .1s timeout sets the framerate of the animation to 10 FPS
            break

        blanks = ' ' * len(status)
        print(f'\r{blanks}\r')

# slow() will be called by the main thread
# This will block the main thread and release GIL, allowing other threads to run
def slow() -> int: 
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
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
