"""
Find the kth largest element in an unsorted array. 
This will be the kth largest element in sorted order, 
not the kth distinct element.

Example

    For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
    kthLargestElement(nums, k) = 6;
    For nums = [99, 99] and k = 1, the output should be
    kthLargestElement(nums, k) = 99.


"""

def heapify(arr, n, i):
    largest = i # init largest as root
    l = 2 * i + 1
    r = 2 * i + 2
    
    # see if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
    
    # if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
        
        
    # change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # heapify the root
        heapify(arr, n, largest)
        
# main function: heapsort
def heapSort(arr):
    n = len(arr)
    
    # build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


def kthLargestElement(arr, k):
    # heap sort
    heapSort(arr)
    
    # get index
    index = len(arr) - k
    
    # return
    return arr[index]


def main():
    arr = [12, 11, 13, 5, 6, 7]
    print(kthLargestElement(arr, 2))
        
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    