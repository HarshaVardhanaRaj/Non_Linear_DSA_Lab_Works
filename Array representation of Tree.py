#node = i, parent = (i-1)/2, left child = 2i+1, right child = 2i+2

arr = ['A','B','C','D','E']

i = int(input("Enter the index of node: "))

if i < len(arr):
    print("Node: ",arr[i])

    #Parent
    if i!=0:
        parent = (i-1)//2
        print("Parent: ",arr[parent])
    else:
        print("This is the Root Node")

    #Left Child
    left = 2*i + 1
    if left < len(arr):
        print("Left Child: ",arr[left])
    else:
        print("No Left Child")

    #Right Child
    right = 2*i + 2
    if right < len(arr):
        print("Right Child: ",arr[right])
    else:
        print("No Right Child")
    
