
def binarySearch(l, target, min=None, max=None):
    if min is None:
        min = 0
    if max is None:
        max = len(l) - 1

    if max < min:
        return -1

    midpoint = (min + max) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binarySearch(l, target, min, midpoint - 1)
    else:
        return binarySearch(l, target, midpoint + 1, max)


l = [1, 3, 5, 7, 10, 12, 15, 20]
target = 12

print(binarySearch(l, target))
