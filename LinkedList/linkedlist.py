

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     

class Linkedlist:
    def __init__(self):
        self.head = None
   

    def printLinkedlist(self):
        while self.head:
            print(f"{self.head.data} ---> ",end="")
            self.head = self.head.next
    
# INSERTING OPERATIONS

    def insertNodeatEnd(self,node):
        while self.head.next is not None:
            self.head = self.head.next
        self.head.next =node

    def insertNodeatFront(self,node):
        if self.head:
            node.next = self.head
            self.head = node    
    def insertafteraNode(self,node,newnode):
        newnode.next = node.next
        node.next=newnode
    
# DELETEING OPERATIONS

    def deletefrombegin(self):
        if self.head:
            self.head =self.head.next
    
    
    def deletefromEnd(self):
        while self.head.next.next is not None:
            self.head = self.head.next
        self.head.next = None

# SEARCHING AN ELEMENT

    def Searchelement(self,ele):
        current = self.head
        while current is not None:
            if current.data == ele:
                return True
            current = self.head.next
        return False
      
#REVERSING LINKEDLIST
    def Reverselinkedlist(self):
        prevpointer= None
        currentpointer = self.head

        
        while currentpointer :
            nextpointer =currentpointer.next
            currentpointer.next=prevpointer
            prevpointer = currentpointer
            currentpointer = nextpointer
        self.head = prevpointer
            
        

       
    
        


   


       



linkedlist = Linkedlist()
linkedlist.head = Node(1)
linkedlist.insertNodeatEnd(Node(3))
linkedlist.insertNodeatFront(Node(4))
linkedlist.insertafteraNode(linkedlist.head,Node(5))
linkedlist.deletefrombegin()
linkedlist.deletefromEnd()
linkedlist.Searchelement(1)
linkedlist.insertNodeatEnd(Node(2))
linkedlist.Reverselinkedlist()

linkedlist.printLinkedlist()










