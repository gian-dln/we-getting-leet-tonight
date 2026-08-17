def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    # binary search
    top, bot = 0, rows
    while top < bot:
        row = (top+bot)//2
        if target > matrix[row][-1]:
            top = row + 1 #look at rows larger
        elif target < matrix[row][0]:
            bot = row
        else:
            break

    if top >= rows:                 
        return False
    row = (top+bot)//2
    l,r = 0, cols
    while l<r:
        m = (l+r)//2
        if target>matrix[row][m]:
            l = m+1
        elif target<matrix[row][m]:
            r = m
        else:
            return True

    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix, target))