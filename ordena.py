import random
from datetime import datetime
import sys
sys.setrecursionlimit(1000000000)
a = 0

def generate_ordered_list(start, end):
    """Generates a list of integers in ascending order from start (inclusive) to end (exclusive).

    Args:
        start: The starting value of the list (inclusive).
        end: The ending value of the list (exclusive).

    Returns:
        A list of integers in ascending order.
    """
    return list(range(start, end))

# Ordered lists with different sizes
wa = generate_ordered_list(1, 1000001) # 1000000 elements
xa = generate_ordered_list(1, 1001)  # 1000 elements
ya = generate_ordered_list(1, 10001)  # 10000 elements
za = generate_ordered_list(1, 100001)  # 100000 elements

def generate_descending_list(start, end):
    return list(range(start, 0, -1))

wd = generate_descending_list(1000000, 0) # 1000000 elements descending
xd = generate_descending_list(1000, 0)  # 1000 elements descending
yd = generate_descending_list(10000, 0)  # 10000 elements descending
zd = generate_descending_list(100000, 0)  # 100000 elements descending

def generate_random_list(size, min_value=0, max_value=1000):
    """Generates a list of random integers within a specified range.

    Args:
        size: The size of the random list.
        min_value: The minimum value (inclusive) for random numbers (default: 0).
        max_value: The maximum value (exclusive) for random numbers (default: 1000).

    Returns:
        A list of random integers.
    """
    return [random.randint(min_value, max_value - 1) for _ in range(size)]

xr = generate_random_list(1000)  # 1000 random elements
yr = generate_random_list(10000)  # 10000 random elements
zr = generate_random_list(100000)  # 100000 random elements
wr = generate_random_list(1000000)  # 1000000 random elements

# Alternatively, generating random lists manually
xr = [random.randint(0, 1000) for _ in range(1000)]
yr = [random.randint(1, 10000) for _ in range(10000)]
zr = [random.randint(0, 100000) for _ in range(100000)]
wr = [random.randint(0, 1000000) for _ in range(1000000)]

def bubbleSort(lst):
    startBubbleSortSecond = datetime.now()
    any = 0
    swap = True
    while swap:
        swap = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
    endBubbleSortSecond = datetime.now()
    diffTimeBubbleSort = endBubbleSortSecond - startBubbleSortSecond
    print(diffTimeBubbleSort)

def selectionSort(lst):
    startSelectionSortSecond = datetime.now()
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    endSelectionSortSecond = datetime.now()
    diffTimeSelectionSort = endSelectionSortSecond - startSelectionSortSecond
    print(diffTimeSelectionSort)

def insertionSort(lst):
    startInsertionSortSecond = datetime.now()
    for i in range(1, len(lst)):
        any = lst[i]
        j = i - 1
        while j >= 0 and any < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = any
    endInsertionSortSecond = datetime.now()
    diffTimeInsertionSort = endInsertionSortSecond - startInsertionSortSecond
    print(diffTimeInsertionSort)

def quickSort(lst, left, right):
    startQuickSortSecond = datetime.now()
    if left < right:
        partitionPosition = partition(lst, left, right)
        quickSort(lst, left, partitionPosition - 1)
        quickSort(lst, partitionPosition + 1, right)
    endQuickSortSecond = datetime.now()
    diffQuickSortTime = endQuickSortSecond - startQuickSortSecond
    print(diffQuickSortTime)

def partition(lst, left, right):
    i = left
    j = right - 1
    pivot = lst[right]
    while i < j:
        while i < right and lst[i] < pivot:
            i += 1
        while j > left and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    if lst[i] > pivot:
        lst[i], lst[right] = lst[right], lst[i]
    return i

def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

def shellSort(lst):
    startShellSortSecond = datetime.now()
    n = len(lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    endShellSortSecond = datetime.now()
    diffTimeShellSort = endShellSortSecond - startShellSortSecond
    print(diffTimeShellSort)

