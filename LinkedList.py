class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self) -> None:
        self.head=None
    def Print_LL(self):
        currnode=self.head
        if currnode is None:
            print("L.L is empty")
        else:
            while currnode:
                print(currnode.val,end='->')
                currnode=currnode.next
    def add_node_start(self,val):
        new=Node(val)
        new.next=self.head
        self.head=new
    def add_node_end(self,val):
         new=Node(val)
         if self.head is None:
            self.head=new
         else:
            lastnode=self.head
            while lastnode.next is not None:
                lastnode=lastnode.next
            lastnode.next=new
    def add_node_afternode(self,curval,val):
        n=self.head
        while n is not None:
            if curval==n.val:
                break
            n=n.next
        if n is None:
            print(f"node is not found and can't insert {val}")
        else:
            new=Node(val)
            new.next=n.next
            n.next=new
    def add_node_beforenode(self,curval,val):
        if self.head is None:
            print('L.L is empty')
            return
        if self.head.val==curval:
            new=Node(val)
            new.next=self.head
            self.head=new
            return
        n=self.head
        while n.next is not None:
            if n.next.val==curval:
                break
            n=n.next
        if n.next is None:
            print(f"Node is not found and can't insert {val}")
        else:
            new=Node(val)
            new.next=n.next
            n.next=new
ll=linkedlist()
ll.add_node_end(10)
ll.add_node_afternode(10,20)
ll.add_node_end(70)
ll.Print_LL()