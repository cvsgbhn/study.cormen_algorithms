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

        return(array)


def binary_search(key, array):
    if len(array) == 1 and array[0] == key:
        return 0
    elif len(array) == 1 and array[0] != key:
        return None

    start_point = len(array)//2
    if key < array[start_point]:
        new_point = binary_search(key, array[:start_point])
    elif key > array[start_point]:
        new_point = binary_search(key, array[start_point:])
    elif key == array[start_point]:
        new_point = start_point
        return new_point


def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    arr = [80, 67, 56, 1234, 456, 0, -6, 45,2345,-50, 48]
    key = 456
    insertion_rec_sort(arr)
    point = binary_search(key, arr)
