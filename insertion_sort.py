#!/usr/bin/env python

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

array = [31, 41, 59, 26,41,58]
insertionSort(array)
for i in range(len(array)): 
    print ("% d" % array[i]) 


#if __name__ == '__main__':
 # main()
