def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for i in range(len(matrix)):
        if binarySearch(matrix[i], target) != -1:
            return True



    return False

def binarySearch(list: list[int], target: int):
    lo,hi = 0, len(list)
    while lo<hi:
        m = lo + ((hi-lo)//2)
        if list[m] >= target:
            hi = m
        elif list[m] < target:
            lo = m+1
    return lo if lo<len(list) and list[lo] == target else -1


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix, target))