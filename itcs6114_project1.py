import random
from time import time
import matplotlib.pyplot as plt


def Merge(ele, l, m, h):
    n1 = m - l + 1
    n2 = h - m

    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = ele[i + l]

    for i in range(n2):
        right[i] = ele[i + 1 + m]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] < right[j]:
            ele[k] = left[i]
            i += 1
        else:
            ele[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        ele[k] = left[i]
        k += 1
        i += 1

    while j < n2:
        ele[k] = right[j]
        k += 1
        j += 1


def mergeSort(ele, l, h):
    if l < h:
        m = (l + h) // 2
        mergeSort(ele, l, m)
        mergeSort(ele, m + 1, h)
        Merge(ele, l, m, h)


def insertionSort(ele):
    for i in range(1, len(ele)):
        key = ele[i]
        j = i - 1

        while j >= 0 and ele[j] > key:
            ele[j + 1] = ele[j]
            j -= 1

        ele[j + 1] = key


def partition(ele, l, h):
    pivot = ele[l]
    i = l + 1
    j = h

    while i < j:
        while i <= h and ele[i] <= pivot:
            i += 1

        while j >= 0 and ele[j] > pivot:
            j -= 1

        if i < j:
            temp = ele[i]
            ele[i] = ele[j]
            ele[j] = temp
        else:
            temp = ele[j]
            ele[j] = pivot
            ele[l] = temp

    return j


def median(ele, low, high, mid):
    a = ele[low]
    b = ele[mid]
    c = ele[high]

    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high
    if b <= c <= a:
        return c, high

    return a, low


def modifiedPartition(ele, l, h):
    pivot, idx = median(ele, l, h, (l + h) // 2)
    i = l + 1
    j = h

    while i < j:
        while i <= h and ele[i] <= pivot:
            i += 1

        while j >= 0 and ele[j] > pivot:
            j -= 1

        if i < j:
            temp = ele[i]
            ele[i] = ele[j]
            ele[j] = temp
        else:
            temp = ele[j]
            ele[j] = pivot
            ele[idx] = temp

    return j


def quickSort(ele, l, h):
    if l < h:
        pi = partition(ele, l, h)
        quickSort(ele, l, pi - 1)
        quickSort(ele, pi + 1, h)


def modifiedQuickSort(ele, l, h):
    if l < h:
        if (h - l) > 15:
            pi = modifiedPartition(ele, l, h)
            quickSort(ele, l, pi - 1)
            quickSort(ele, pi + 1, h)
        else:
            for i in range(l + 1, h + 1):
                key = ele[i]
                j = i - 1

                while j >= l and ele[j] > key:
                    ele[j + 1] = ele[j]
                    j -= 1

                ele[j + 1] = key


def heapify(ele, i, n):
    l = 2 * i + 1
    h = 2 * i + 2
    j = i

    if l < n and ele[l] > ele[i]:
        i = l

    if h < n and ele[h] > ele[i]:
        i = h

    if i != j:
        ele[i], ele[j] = ele[j], ele[i]
        heapify(ele, i, n)


def heapSort(ele, l, h):
    n = len(ele)

    for i in range(n // 2, -1, -1):
        heapify(ele, i, n)

    for i in range(n - 1, 0, -1):
        ele[i], ele[0] = ele[0], ele[i]
        heapify(ele, 0, i)


sizes = [15, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
quicksorttime = {}
mergesorttime = {}
insertionsorttime = {}
heapsorttime = {}
modifiedquicksorttime = {}

quicksorttimesorted = {}
mergesorttimesorted = {}
insertionsorttimesorted = {}
heapsorttimesorted = {}
modifiedquicksorttimesorted = {}

quicksorttimereverse = {}
mergesorttimereverse = {}
insertionsorttimereverse = {}
heapsorttimereverse = {}
modifiedquicksorttimereverse = {}

for i in sizes:
    ele = []
    for x in range(i):
        ele.append(random.randint(1, 1000))

    temp = ele
    t = time()
    mergeSort(temp, 0, len(temp) - 1)
    t = time() - t
    mergesorttime[i] = t

    temp = sorted(ele)
    t = time()
    mergeSort(temp, 0, len(temp) - 1)
    t = time() - t
    mergesorttimesorted[i] = t

    temp = sorted(ele)[-1::-1]
    t = time()
    mergeSort(temp, 0, len(temp) - 1)
    t = time() - t
    mergesorttimereverse[i] = t

    temp = ele
    t = time()
    insertionSort(temp)
    t = time() - t
    insertionsorttime[i] = t

    temp = sorted(ele)
    t = time()
    insertionSort(temp)
    t = time() - t
    insertionsorttimesorted[i] = t

    temp = sorted(ele)[-1::-1]
    t = time()
    insertionSort(temp)
    t = time() - t
    insertionsorttimereverse[i] = t

    temp = ele
    t = time()
    quickSort(temp, 0, len(temp) - 1)
    t = time() - t
    quicksorttime[i] = t

    temp = sorted(ele)
    t = time()
    quickSort(temp, 0, len(temp) - 1)
    t = time() - t
    quicksorttimesorted[i] = t

    temp = sorted(ele)[-1::-1]
    t = time()
    quickSort(temp, 0, len(temp) - 1)
    t = time() - t
    quicksorttimereverse[i] = t

    temp = ele
    t = time()
    modifiedQuickSort(temp, 0, len(temp) - 1)
    t = time() - t
    modifiedquicksorttime[i] = t

    temp = sorted(ele)
    t = time()
    modifiedQuickSort(temp, 0, len(temp) - 1)
    t = time() - t
    modifiedquicksorttimesorted[i] = t

    temp = sorted(ele)[-1::-1]
    t = time()
    modifiedQuickSort(temp, 0, len(temp) - 1)
    t = time() - t
    modifiedquicksorttimereverse[i] = t

    temp = ele
    t = time()
    heapSort(temp, 0, len(temp) - 1)
    t = time() - t
    heapsorttime[i] = t

    temp = sorted(ele)
    t = time()
    heapSort(temp, 0, len(temp) - 1)
    t = time() - t
    heapsorttimesorted[i] = t

    temp = sorted(ele)[-1::-1]
    t = time()
    heapSort(temp, 0, len(temp) - 1)
    t = time() - t
    heapsorttimereverse[i] = t

plt.plot(list(mergesorttime.keys()), list(mergesorttime.values()), "r")
plt.plot(list(quicksorttime.keys()), list(quicksorttime.values()), "g")
plt.plot(list(modifiedquicksorttime.keys()), list(modifiedquicksorttime.values()), "b")
plt.plot(list(insertionsorttime.keys()), list(insertionsorttime.values()), "y")
plt.plot(list(heapsorttime.keys()), list(heapsorttime.values()), "m")
plt.title("Random Numbers")
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.show()

plt.plot(list(mergesorttimesorted.keys()), list(mergesorttimesorted.values()), "r")
plt.plot(list(quicksorttimesorted.keys()), list(quicksorttimesorted.values()), "g")
plt.plot(list(modifiedquicksorttimesorted.keys()), list(modifiedquicksorttimesorted.values()), "b")
plt.plot(list(insertionsorttimesorted.keys()), list(insertionsorttimesorted.values()), "y")
plt.plot(list(heapsorttimesorted.keys()), list(heapsorttimesorted.values()), "m")
plt.title("Sorted Numbers")
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.show()

plt.plot(list(mergesorttimereverse.keys()), list(mergesorttimereverse.values()), "r")
plt.plot(list(quicksorttimereverse.keys()), list(quicksorttimereverse.values()), "g")
plt.plot(list(modifiedquicksorttimereverse.keys()), list(modifiedquicksorttimereverse.values()), "b")
plt.plot(list(insertionsorttimereverse.keys()), list(insertionsorttimereverse.values()), "y")
plt.plot(list(heapsorttimereverse.keys()), list(heapsorttimereverse.values()), "m")
plt.title("Reverse Sort")
plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.show()
