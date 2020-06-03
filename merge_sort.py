n = [3,21,4,7,33,1,43,8]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def selection_sort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i], arr[min_id] = arr[min_id],arr[i]


def conc(**kwargs):
    result = ""
    for kw in kwargs.values():
        result += kw
    return result

print(conc(a="Real", b="Python", c="Is", d="Great", e="!"))
