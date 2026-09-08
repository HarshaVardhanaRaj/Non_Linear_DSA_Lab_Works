def bin_search(a, key, low, high):

    if low > high:
        print("Element Not Found")
        return

    mid = (low + high) // 2

    if a[mid] == key:
        print("Element Found")
        return

    elif a[mid] < key:
        return bin_search(a, key, mid + 1, high)

    else:
        return bin_search(a, key, low, mid - 1)


key = int(input("Enter an element to search: "))

bin_search([1,2,3,4,5,6,7,8], key, 0, 7)
                                        
