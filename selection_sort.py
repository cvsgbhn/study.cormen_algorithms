#!/usr/bin/env python

def selectionSortDesc(array):
    for j in range(len(array)):
        min1 = array[j]
        for i in range(len(array)):
            if array[i] < min1:
                min1 = array[i]
                array[i] = array[j]
                array[j] = min1

def selectionSortAsc(array):
    for j in range(len(array)):
        min1 = array[j]
        for i in range(j + 1, len(array)):
            if array[i] < min1:
                min1 = array[j]
                array[j] = array[i]
                array[i] = min1



array = [31, 41, 59, 26,41,58]
selectionSortDesc(array)
for i in range(len(array)): 
    print ("% d" % array[i]) 

selectionSortAsc(array)
for i in range(len(array)): 
    print ("% d" % array[i]) 



#if __name__ == '__main__':
 # main()
