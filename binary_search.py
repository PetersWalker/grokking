# implemenation of binary search
import math


def search(array, value):
    # i and j are search space, pivot is midway
    i = 0
    pivot = math.floor(len(array)/2)
    j = len(array)

    while i < j:
        if value > array[pivot]:
            i = pivot + 1
            pivot = (math.floor((j - i)/2)) + i
        if value < array[pivot]:
            j = pivot - 1
            pivot = (math.floor((j - i)/2)) + i
        if value == array[pivot]:
            return pivot

    return None
