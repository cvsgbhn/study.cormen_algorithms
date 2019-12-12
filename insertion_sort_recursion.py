def insertion_rec_sort(array):
    if len(array) > 1:
        arr_1 = array[:-1]
        insertion_rec_sort(arr_1)

        for el in range(len(arr_1)):
            array[el] = arr_1[el]

        j = len(array) - 1
        key = array[j]
        while j > 0 and key < array[j - 1]:
            temp = array[j - 1]
            array[j - 1] = key
            array[j] = temp
            j -= 1
        #array[j - 1] = key

        return array


def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()


if __name__ == '__main__':
    arr = [80, 67, 56, 1234, 456, 0, -6, 45]
    print("Given array is", end="\n")
    printList(arr)
    insertion_rec_sort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
