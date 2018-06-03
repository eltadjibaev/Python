
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def reverse(self, head, k):
        current=head
        next=None
        prev=None
        cnt=0

        while current!=None and cnt<k:
            next=current.next
            current.next=prev
            prev=current
            current=next
            cnt+=1

        if next!=None:
            head.next=self.reverse(next, k)

        return prev

    def append(self, data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return

        last=self.head
        while last.next:
            last=last.next

        last.next=newNode

    def printList(self):
        node=self.head
        while node:
            print(node.data, end=' ')
            node=node.next
        print()

list=LinkedList()

for n in range(1, 10):
    list.append(n)

list.printList()
list.head=list.reverse(list.head, 3)
list.printList()





















