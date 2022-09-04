
def selectionSort(arr):

    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min] , arr[i] =  arr[i], arr[min]
    return arr
    

if __name__ == '__main__':
    arr = [4, 5, 2, 3, 6, 1, 9, 7, 8]
    print(f'Unsorted array: {arr}')
    print(f'Sorted array: {selectionSort(arr)}')
    