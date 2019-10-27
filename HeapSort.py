def heapSort():
    arr_len = arr.__len__()
    heapify(arr_len)
    for i in range(arr_len - 1, -1, -1):
        swap(0, i)
        arr_len -= 1
        heapify(arr_len)


def swap(src, dest):
    tmp = arr[src]
    arr[src] = arr[dest]
    arr[dest] = tmp


def heapify(arr_len):
    for i in range(int(arr_len / 2) - 1, -1, -1):
        rightChild = 2 * i + 2
        leftChild = 2 * i + 1
        if rightChild <= arr_len - 1\
                and arr[rightChild] > arr[leftChild] and arr[i] < arr[rightChild]:
            swap(i, rightChild)
        elif arr[i] < arr[leftChild]:
            swap(i, leftChild)
    return arr


if __name__ == "__main__":
    arr = [6, 1, 9, -5, -55, 4, 0, 70, 22, -100, 69, 11, -7, 2, 44, -23, -1, -4, 999]
    print(arr)
    heapSort()
    print(arr)
