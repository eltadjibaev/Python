
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data, end=' ')
            temp=temp.next
        print('\n', end='')

    def push(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def insertAfter(self, prevNode, data):
        if prevNode==None:
            print('No prev Node')
            return

        newNode = Node(data)

        newNode.next=prevNode.next
        prevNode.next=newNode

    def append(self, data):
        newNode=Node(data)

        if self.head==None:
            self.head=newNode
            return

        last=self.head
        while last.next:
            last=last.next

        last.next=newNode

    def deleteNode(self, key):
        temp=self.head

        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return

        while temp:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next

        if temp==None:
            return

        prev.next=temp.next
        temp=None

    def deleteNodePosition(self, pos):
        if self.head==None:
            return

        temp=self.head

        if pos==0:
            self.head=temp.next
            temp=None
            return

        for i in range(pos-1):
            temp=temp.next
            if temp is None:
                return

        if temp.next==None:
            return

        next=temp.next.next

        temp.next=None
        temp.next=next

    def getCountRec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    def getCount(self):
        return self.getCountRec(self.head)



if __name__=='__main__':
    list=Linkedlist()
    list.append(6)
    list.push(7)
    list.push(1)
    list.append(4)
    list.insertAfter(list.head.next, 8)
    list.print_list()
    # list.deleteNodePosition(3)
    # list.print_list()
    print(list.getCount())