import random

data1 = [random.randint(1, 100) for _ in range(100)]
unique_data = list(set(data1))


print(unique_data)

#binay search
def binary_search(data, target):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == data[mid]:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1


#insertion_sort

def insertion_sort(data):
    for i in range (1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and j > key:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key
    return data

#quick_sort

def quick_sort(data, low, high):
    if low < high:
        pivot_index = partition(data,low, high)

        quick_sort(data, low, pivot_index-1)
        quick_sort(data, pivot_index+1, high)

def partition(data,low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]

    data[i+1], data[high] = data[high], data[i+1]
    return i + 1

quick_sort(data1, 0, len(data1) -1)















