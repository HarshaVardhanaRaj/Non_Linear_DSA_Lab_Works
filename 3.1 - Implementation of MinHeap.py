class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self,i):
        return ((i-1)//2)

    def left(self,i):
        return (2*i + 1)

    def right(self,i):
        return (2*i + 2)

    def swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j] , self.heap[i]

    def insert(self, val):
        self.heap.append(value)
        self.upheap(len(self.heap)-1)

    def upheap(self, i):
        while i>0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i,self.parent(i))
            i = self.parent(i)
            
    def delete_min(self):
        if len(self.heap)==0:
            return None

        if len(self.heap)==1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.downheap(0)

        return root

    def downheap(self,i):
        size = len(self.heap)

        while True:
            smallest  = i
            left = self.left(i)
            right = self.right(i)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest!=i:
                self.swap(i,smallest)
                i = smallest
            else:
                break

    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def display(self):
        print("Heap: ",self.heap)


#main program
choice = 0
h = MinHeap()
                                                                     
print("\n--- Binary Min Heap Operations ---")
print("1. Insert")
print("2. Delete Minimum")
print("3. Get Minimum")
print("4. Display Heap")
print("5. Exit")

while choice!=5:
    choice = int(input("\nEnter your choice: "))

    if choice==1:
        value = int(input("Enter element: "))
        h.insert(value)
        print("\nElement inserted")

    if choice==2:
        item = h.delete_min()
        if item is None:
            print("\nHeap is empty")
        else:
            print("\nDeleted element = ",item)

    if choice==3:
        item = h.get_min()
        if item is None:
            print("\nHeap is empty")
        else:
            print("\nMinimum element = ",item)

    if choice==4:
        h.display()

    if choice>5 or choice<=0: #choice = 6,7,8,etc.
        print("\nInvalid choice. Try again.")
