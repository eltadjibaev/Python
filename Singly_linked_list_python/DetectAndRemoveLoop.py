
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def detectAndRemoveLoop(self):
        if self.head==None or self.head.next==None:
            return

        slow=self.head.next
        fast=self.head.next.next

        while fast!=None:
            if fast.next==None:
                break
            if slow is fast:
                break
            slow=slow.next
            fast=fast.next.next

        if slow is fast:
            slow=self.head
            while slow.next!=fast.next:
                slow=slow.next
                fast=fast.next

            fast.next=None

    def push(self, data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return

        newNode.next=self.head
        self.head=newNode

    def printList(self):
        node=self.head
        while node is not None:
            print(node.data, end=' ')
            node=node.next
        print()

list=LinkedList()
for i in range(10, 60, 10):
    list.push(i)

#Create a loop for testing
list.head.next.next.next.next.next=list.head.next.next

list.detectAndRemoveLoop()

list.printList()