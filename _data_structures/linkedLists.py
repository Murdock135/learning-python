class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        curNode = self.head

        while curNode.next!=None:
            curNode = curNode.next
        curNode.next = newNode

    def length(self):
        curNode = self.head
        total = 0

        while curNode.next!=None:
            total = total + 1
            curNode = curNode.next
            
        return total

    def display(self):
        elems = []
        curNode = self.head
        while curNode.next!=None:
            curNode = curNode.next
            elems.append(curNode.data)
        print(elems)

myList = linkedList()
myList.append(1)
myList.append(6)
myList.display()




