class Node:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right= None
    
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        print(self.data)
    
    
#Inorder,PreOrder,PostOrder Traversals  

    def PreorderTrasversal(self):
        print(self.data)
        if self.left:
            self.left.PreorderTrasversal()
        if self.right:
            self.right.PreorderTrasversal()
   
    def InorderTraversal(self):
        if self.left:
            self.left.InorderTraversal()
        print(self.data)
        if self.right:
            self.right.InorderTraversal()

    def PostOrderTraversal(self):
        if self.left:
            self.left.PostOrderTraversal()
        if self.right:
            self.right.PostOrderTraversal()
        print(self.data)
    
      
tree=Node(2)
tree.left=Node(3)
tree.right=Node(4)
tree.insert(5)
tree.PrintTree()
tree.PostOrderTraversal()
