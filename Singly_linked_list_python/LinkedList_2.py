
class LinkedList(object):
    def __init__(self):
        self.head=None

    class Node(object):
        def __init__(self, d):
            self.data=d
            self.next=None

    def swapNodes(self, x, y):
        if x==y:
            return

        prevX=None
        currX=self.head
        while currX!=None and currX.data!=x:
            prevX=currX
            currX=currX.next

        prevY=None
        currY=self.head
        while currY!=None and currY.data!=y:
            prevY=currY
            currY=currY.next

        if currY == None or currX == None:
            return

        if prevX != None:
            prevX.next=currY
        else:
            self.head=currY

        if prevY != None:
            prevY.next=currX
        else:
            self.head=currX

        tmp=currX.next
        currX.next=currY.next
        currY.next=tmp

    def reverseUTIL(self, curr, prev):
        if curr.next==None:
            self.head=curr
            curr.next=prev
            return

        next=curr.next
        curr.next=prev
        self.reverseUTIL(next, curr)

    def reverse(self):
        if self.head==None:
            return
        self.reverseUTIL(self.head, None)

    def push(self, data):
        newNode=self.Node(data)
        newNode.next=self.head
        self.head=newNode

    def printList(self):
        node=self.head
        while node != None:
            print(node.data, end=' ')
            node=node.next
        print('\n', end='')

list = LinkedList()

list.push(7)
list.push(6)
list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

list.printList()
list.swapNodes(2, 7)
list.printList()
list.reverse()
list.printList()