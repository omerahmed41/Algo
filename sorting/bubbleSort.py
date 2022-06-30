
def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]> arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
    

if __name__ == '__main__':

    arr = [4,5,2,3,6,1,9,7,8]
    print(f'Unsorted array: {arr}')
    print(f'Sorted array: {bubbleSort(arr)}')