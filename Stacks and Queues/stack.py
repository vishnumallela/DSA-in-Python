#A stack is a linear data structure that follows the principle of "Last In First Out (LIFO)". 
#This means the last element inserted inside the stack is removed first.
#methods-Push,Pop,isEmpty,isFull,Peek


#Creating Stack
def Create_stack():
    stack=[]
    return stack
#Adding element to Stack
def addto_stack(stack,item):
    stack.append(item)
#pop element from stack
def pop_stack(stack):
    stack.pop()
    
    




stack = Create_stack()
addto_stack(stack,2)
pop_stack(stack)
try:
    if len(stack) == 0:
        print("stack is empty")
    else:
        print(stack)
except:
    print("error occured")
    