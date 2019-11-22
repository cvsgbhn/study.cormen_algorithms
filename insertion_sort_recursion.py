def insertion_rec_sort(array):
    if len(array) > 1:
        true_ar = array[:-1]
        insertion_rec_sort(true_ar)
        
        j = len(true_ar)
        key = array[j]
        while j >= 0 and key < true_ar[j - 1]: 
            array[j] = true_ar[j - 1] 
            j -= 1
        true_ar[j - 1] = key
        
        for i in range(len(true_ar)):
            array[i] = true_ar[i]
        
      
        
        


def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
if __name__ == '__main__': 
    arr = [2,80,67,5,4,123,1]  
    print ("Given array is", end="\n")  
    printList(arr) 
    insertion_rec_sort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
