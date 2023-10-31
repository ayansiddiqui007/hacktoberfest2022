class Node:
    def __init__(self,v=None):
        self.value=v
        self.next=None
        return
    def isempty(self):
        if self.value==None:
            return(True)
        else:
            return(False)
    def append(self,v):
        if self.isempty():
            self.value=v
        elif self.next==None:
            self.next=Node(v)
        else:
            self.next.append(v)
        return
    def appendi(self,v):
        if self.isempty():
            self.value=v
            return
        temp=self
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(v)
        return
    def insert(self,v):
        if self.isempty():
            self.value=v
            return 
        newnode=Node(v)
        (self.value,newnode.value)=(newnode.value,self.value)
        (self.next,newnode.next)=(newnode,self.next)
        return 
    def delete(self,v):
        if self.isempty():
            return
        if self.value==v:
            self.value=None
            if self.next!=None:
                self.value=self.next.value
                self.next=self.next.next
            return
        else:
            if self.next!=None:
                self.next.delete(v)
                if self.next.value==None:
                    self.next=None
        return
    def display(self):
        if self.isempty()==True:
            print('None')
        else:
            temp=self
            while temp!=None:
                print(temp.value,end="  ")
                temp=temp.next
head=Node(10)
head.append(20)
head.append(30)
head.appendi(40)
head.appendi(50)
head.delete(30)
head.display()