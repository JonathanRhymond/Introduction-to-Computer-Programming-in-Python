#1
def path_d(n):
    result = {}
    result[0] = [1]
    for row in range(1,n-1):
        result[row] = [row-1,row+1]
    result[n-1] = [n-2]
    return result