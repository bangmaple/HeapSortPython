def heapSort():
    arr_len = arr.__len__()
    buildHeap(arr_len)
    for i in range(arr_len-1, -1, -1):
        swap(0, i)
        arr_len -= 1
        buildHeap(arr_len)


def buildHeap(arr_len):
    for i in range(int(arr_len / 2) - 1, -1, -1):
        reheapify(i, arr_len)
    return arr


def swap(i, child):
    tmp = arr[i]
    arr[i] = arr[child]
    arr[child] = tmp


def reheapify(i, arr_len):
    leftChild = 2 * i + 2
    rightChild = 2 * i + 1
    if leftChild <= arr_len - 1:
        if arr[leftChild] > arr[rightChild]:
            if arr[i] < arr[leftChild]:
                swap(i, leftChild)
        else:
            if arr[i] < arr[rightChild]:
                swap(i, rightChild)
    else:
        if arr[i] < arr[rightChild]:
            swap(i, rightChild)


if __name__ == "__main__":
    arr = [6, 1, 9, -5, -55, 4, 0, 70, 22, -100, 69, 11]
    print(arr)
    heapSort()
    print(arr)