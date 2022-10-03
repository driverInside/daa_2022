'''
linear search O(n)
'''
def linear_search(arr, e):
    for i in range(len(arr)):
        if e == arr[i]: return i
    return -1
    
if __name__ == "__main__":
    arr = [2, 5, 3, 8, 6, 1]
    element_index = linear_search(arr, 7)
    
    print(element_index)
    