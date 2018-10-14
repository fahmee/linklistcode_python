class Node:
   def __init__(self,data):
       self.data=data
       self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            lastnode = self.head
            while True:
                # print("linklist")

                if(lastnode.next==None):
                    break
                else:
                    lastnode=lastnode.next
            lastnode.next=newnode




    def Print(self):
        lastnode=self.head
        while True:
            # print("print")
            if(lastnode==None):
                break
            else:
                print(lastnode.data,end="=>")
                lastnode=lastnode.next
        print("None")
    def firstinsert(self,newnode):
        # temp=self.head
        # self.head=newnode
        # newnode.next=temp
        newnode.next=self.head
        # print(self.head.data)
        # print(newnode.next.data)
        self.head=newnode
        # print(self.head.data)

    def middle_insert(self,newnode,a):
        lastnode=self.head
        c=1
        while True:
            if(lastnode==None):
                print("linklist is not that much bigger")
                break
            elif(a>c+1):
                c+=1
                lastnode=lastnode.next
            elif(a==c+1):
                newnode.next=lastnode.next
                lastnode.next=newnode
                # newnode.next=temp
                break
    def lengthlist(self):
        c=0
        lastnode=self.head
        while True:
            if(lastnode==None):
                return(c)
                break
            else:
                c+=1
                lastnode=lastnode.next
    def delnode(self,n):
        lastnode=self.head
        c=1
        while True:
            if(n==1):
                temp=lastnode.next
                self.head=temp
                break
            elif(lastnode==None):
                print("that node does not exixt")
                break
            elif(c+1<n):
                lastnode=lastnode.next
                c+=1
            elif(c+1==n):
                temp=lastnode.next.next
                # lastnode.next=None
                lastnode.next=temp
                break
class merg_2_list_sorted:
    def __init__(self):
        self.head = None
    def recive_linklist(self,linklist,linklist1):
        self.head=linklist.head
        del linklist.head
        lastnode = self.head
        while lastnode.next!=None:
            lastnode=lastnode.next
        lastnode.next=linklist1.head
        del linklist1.head

        # lnode = self.head
        currentnode=self.head

        while currentnode!=None:
            min = currentnode.data
            lnode=currentnode
            while lnode!=None:
                # print(min,lnode.data)
                if(min>lnode.data):
                    min=lnode.data
                    currentnode.data,lnode.data=lnode.data,currentnode.data
                lnode=lnode.next
            currentnode=currentnode.next

    def Print(self):
        lastnode1 = self.head
        while True:
            if(lastnode1==None):
                break
            else:
                print(lastnode1.data, end="=>")
                lastnode1=lastnode1.next
        print("None")




















newnode=Node("2")
linklist=Linklist()
linklist.insert(newnode)
newnode=Node("4")
linklist.insert(newnode)
newnode=Node("6")
linklist.firstinsert(newnode)
newnode=Node("3")
linklist.insert(newnode)
newnode=Node("1")
linklist.middle_insert(newnode,5)
# linklist.Print()
linklist1=Linklist()
newnode=Node("7")
linklist1.insert(newnode)
newnode=Node("5")
linklist1.insert(newnode)
newnode=Node("9")
linklist1.insert(newnode)



# print(linklist.lengthlist())
# linklist.delnode(1)
linklist.Print()
linklist1.Print()
new_list=merg_2_list_sorted()
new_list.recive_linklist(linklist,linklist1)
new_list.Print()