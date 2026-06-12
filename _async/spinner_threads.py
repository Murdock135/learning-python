'''
This program runs a script and displays a spinner '\|/' while the program is running.

- The spin() and slow() will run concurrently
- The main thread-- The only thread when the program starts- will start a new thread to run spin() and slow()

Program Flow:
1. Initialization:
    1.1 Event 'done' is instantiated
    1.2 Thread 'spinner' is instantiated
2. Start:
    2.1 spinner thread is started. But the GIL is still held by main thread. So nothing happens
    2.2 slow() makes the main thread sleep for 3 seconds.
3. Main Thread sleeps. During this time:
    3.1 GIL is passed to spinner thread. 
    3.2 For loop:
        i. char = one of {\,|,/}
        ii. char is printed instantly
        iii. done.set(0.1) makes the Event wait for 0.1s and then check if done.set() == True
        iv. ...run loop again since done.wait() == False
4. Main thread wakes up (time.sleep(3) finishes)
    4.1 done.set() turns internal flag to True
5. spinner.join() gives the GIL to the spinner thread.
    5.1 Enter the for loop
    5.2 Print char
    5.3 done.wait() waits for 0.1s and then evaluates to True
    5.4 break out of loop



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
