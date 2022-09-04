def merge_sort(arr):
    def merge(l, r):

        i = j = k = 0

        # Copy data to temp arrays l[] and r[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        merge(L, R)
    return arr


# Code to print the list


if __name__ == '__main__':
    arr = [4, 5, 2, 3, 6, 1, 9, 7, 8]
    print(f'Unsorted array: {arr}')
    print(f'Sorted array: {merge_sort(arr)}')
