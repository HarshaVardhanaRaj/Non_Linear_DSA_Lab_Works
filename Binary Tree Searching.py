class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
        
    else: #key > root.data
        root.right = insert(root.right, key)

    return root


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)
        
    elif key > root.data:
        root.right = delete(root.right, key)
        
    else:

        #no children
        if root.left is None and root.right is None:
            return None

        #1 child
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        #2 children
        else: 
            sub = find_min(root.right)
            root.data = sub
            root.right = delete(root.right, sub)

    return root


def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def find_min(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root.data


def find_max(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.data


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

root = None
a=0

print("\nBinary Search Tree Operations: \n1 - Insert \n2 - Delete \n3 - Search \n4 - Find Max \n5 - Find Min \n6 - Display \n7 - Exit \n")

while(a!=7):
    
    a = int(input("Enter your choice: "))

    if a==1:
        val = int(input("Enter the value: "))
        root = insert(root,val)
        print("Element Inserted\n")

    if a==2:
        element = int(input("Enter the element to be deleted: "))
        root = delete(root,element)
        print("Element Deleted\n")

    if a==3:
        num = int(input("Enter a num to search: "))
        res = search(root,num)
        if res is None:
            print("Not Found\n")
        else:
            print("Found\n")

    if a==4:
        maxv = find_max(root)
        print("Maximum Value = ",maxv,"\n")

    if a==5:
        minv = find_min(root)
        print("Minimum Value = ",minv,"\n")

    if a==6:
        print("In-Order: ", end="")
        in_order(root)
        print("\n")
