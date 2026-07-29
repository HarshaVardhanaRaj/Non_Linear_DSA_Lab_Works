
class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
                                                                                                                                           
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

print("Root: ",root.data)
print("Left Child: ",root.left.data)
print("Right Child: ",root.right.data)    


def level_order(root):
    if root is None:
        return

    queue = [root] #inserting root node into queue

    while len(queue) > 0:                                                                                                                    
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)
                
        if current.right:
            queue.append(current.right)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=" ")

print("\n\nLevel Order: ", end=" ")
level_order(root)
print("\n")
    
print("In Order: ", end=" ")
in_order(root)
print("\n")
    
print("Pre Order: ", end=" ")
pre_order(root)
print("\n")

print("Post Order: ", end=" ")
post_order(root)
print("\n")
