#!/usr/bin/env python

def merge_sort(array):
    if len(array) > 1:
        middle = len(array)//2
        left_a = array[:middle]
        right_a = array[middle:]
    
        merge_sort(left_a)
        merge_sort(right_a)
    
        i = j = k = 0
    
        while i < len(left_a) and j < len(right_a):
            if left_a[i] < right_a[j]:
                array[k] = left_a[i]
                i += 1
            else:
                array[k] = right_a[j]
                j += 1
            k += 1
    
        while i < len(left_a) and k < len(array):
            array[k] = left_a[i]
            k += 1
            i += 1
        
        while j < len(right_a) and k < len(array):
            array[k] = right_a[j]
            k += 1
            i += 1



def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
if __name__ == '__main__': 
    arr = [1,2,3,4,5,5,4,3,2,1]  
    print ("Given array is", end="\n")  
    printList(arr) 
    merge_sort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

