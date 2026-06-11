'''
Key Topic: Coutines
-------------------------
source: Fluent Python 2 ed.

This program uses python's [asyncio] module to run a script and displays a spinner '\|/' while the program is running.

- Starting with the main() and then supervisor() makes the code easier to understand.
- The spin() and slow() will run concurrently


Additional info:
- It is the job of the OS schedulers to allocate CPU time to drive threads and processes.
- In contrast, coroutines are driven by an application-level 'event-loop' that manages a queue of pending coroutines.
- Each coroutine in the event-loop are driven sequentially.
- event-loop monitors I/O ops initiated by coroutines and passes back control to the corresponding coroutine when I/O completes
- [IMPORTANT]: The event-loop, library coroutines and user coroutines all execute in a single thread.
- The implication of the previous bullet is that coroutines cannot run in parallel, thus slowing down the event loop.

Notes on asyncio
- asyncio.run() starts the event-loop to drive the coroutine that will eventually set other
coroutines in motion
- main() will stay blocked until supervisor returns.
- Native coroutines are defined with the 'async' keyword.
- use asyncio.sleep() instead of time.sleep() to not block other coroutines (recall the coroutines are in the same thread)
'''

import itertools
import asyncio

def main() -> None: # regular function
    result = asyncio.run(supervisor()) # Method 1- asyncio.run(coro()): Called from a regular function. This blocks main() until done
    print(f'Answer: {result}')

async def supervisor() -> int: # coroutine
    spinner = asyncio.create_task(spin('thinking!')) # Method 2- asyncio.create_task(): This is called from a coroutine to schedule another coroutine. This does NOT block the calling function 
    print(f'spinner object: {spinner}')

    result = await slow() # Method 3- await coro(): slow() will run, blocking supervisor()

    spinner.cancel() # This will raise a asyncio.CancelledError

    return result

async def spin(msg: str) -> None: # This will run in a separate thread
    for char in itertools.cycle(r'\|/-'): # This will yield an infinite loop because itertools.cycle() cycles infinitely
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break

        blanks = ' ' * len(status)
        print(f'\r{blanks}\r')

# slow() will be called by the main thread
# This will block the main thread and release GIL, allowing other threads to run
async def slow() -> int: 
    await asyncio.sleep(3)

    # import time
    # time.sleep(3)
    return 42


if __name__ == '__main__':
    main()
