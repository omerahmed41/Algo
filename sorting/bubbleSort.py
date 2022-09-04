
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
    

if __name__ == '__main__':

    array = [4, 5, 2, 3, 6, 1, 9, 7, 8]
    print(f'Unsorted array: {array}')
    print(f'Sorted array: {bubble_sort(array)}')


