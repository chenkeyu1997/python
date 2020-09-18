class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class linkOne(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def isEmpty(self):
        return self.count==0
    def size(self):
        return self.count
    def addElementToTail(self,data):
        if(self.tail!= None):
            temp = Node(data,None)
            self.tail.next = temp
            self.tail = temp
            self.count += 1
        else:
            self.head=self.tail=Node(data,None)
            self.count+=1
    def DeleteElementFromTail(self):

        if(self.head==self.tail):
            self.count=0
            self.head=self.tail=None
        else:
            temp = self.tail
            t = self.head
            while(t.next!=self.tail):
                t = t.next
            self.tail=t
            self.count -= 1
            del temp
        return temp.data

lk = linkOne()
lk.addElementToTail(10)
lk.addElementToTail(20)
lk.addElementToTail(30)
lk.addElementToTail(40)
a = lk.size()
b = lk.tail.data
c = lk.head.next.next.data
print(a)
print(b)
print(c)

