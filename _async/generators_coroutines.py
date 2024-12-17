#Generators
# from typing import Iterable


def countdown(n):
	while n>0:
		yield n
		n-=1

x = countdown(10)

#printing the generator
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(next(x))

# #CO ROUTINES
# def finder(x):
#     while True:
#         inputText = yield
#         if x in inputText:
#             print(inputText)

# f = finder('python')
# print(f)
# f.send(None)
# f.send('some text including python')
# f.close()

#CHAINING CO ROUTINES

def producer(sentence, next_coroutine):
    tokens = sentence.split(" ")

    for token in tokens:
        next_coroutine.send(token)
    
    next_coroutine.close()

def pattern_filter(pattern='ing', next_coroutine=None):
    print(f'searching for {pattern}')

    try:
        while True:
            token = yield
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print('Done with filtering')

def print_token():
    print('I\'m a sink. I print tokens')
    try:
        while True:
            token = yield
            print(token)
    except GeneratorExit:
        print('Done with printing')

pt = print_token() 
pt.__next__() 
pf = pattern_filter(next_coroutine = pt) 
pf.__next__() 
  
sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)       