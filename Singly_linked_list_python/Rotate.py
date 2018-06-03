
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def rotate(self, k):
        if k==0:
            return

        node=self.head
        cnt=1
        while cnt<k and node is not None:
            node=node.next
            cnt+=1

        if node is None:
            return

        keyNode=node

        while node.next is not None:
            node=node.next

        node.next=self.head
        self.head=keyNode.next
        keyNode.next=None

    def push(self, data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return

        newNode.next=self.head
        self.head=newNode

    def printList(self):
        n=self.head
        while n is not None:
            print(n.data, end=" ")
            n=n.next
        print()

list=LinkedList()

for i in range(60, 0, -10):
    list.push(i)

list.printList()
list.rotate(4)
list.printList()

