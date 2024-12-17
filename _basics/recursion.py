#call stack
def A():
    return "hello "+B()

def B():
    return "my "+C()

def C():
    return "friends"

print(A())

#call stack is relevant in recursion. The stack overflows if you don't keep a base case


