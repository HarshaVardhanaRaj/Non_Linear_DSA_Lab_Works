def bin_search(a, key, low, high):
    
    while(low<=high):    
        mid = (low + high) // 2

        if a[mid] == key:
            print("Element Found")
            return

        elif a[mid] < key:
            low = mid +1

        else:
            high = mid-1

    
    print("Element Not Found")
    return


key = int(input("Enter an element to search: "))

bin_search([1,2,3,4,5,6,7,8], key, 0, 7)
                                        
