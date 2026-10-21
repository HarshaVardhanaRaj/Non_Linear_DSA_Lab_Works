def quick_sort(array, low, high):
    if low<high:
        p = array[low]
        i = low+1
        j = high
        
        while i<=j:
            while i<=j and array[i]<=p:
                i+=1
            while i<=j and array[j]>=p:
                j-=1
            if i<j:
                array[i], array[j] = array[j], array[i]
                
        array[low], array[j] = array[j], array[low]
        quick_sort(array, low, j-1)
        quick_sort(array, j+1, high)
    
    return array

A = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(A, 0, len(A)-1))