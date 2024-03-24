#1
def anti_diag(n):
    result = []
    for row in range(n):
        result.append([0]*n)
    for i in range(n):
        result[i][n-1] += 1
        n -= 1
    return result

#2
def small_plus(n):
    result = []
    for row in range(n):
        result.append([0]*n)
    result[n//2][n//2] = 1
    result[(n//2)+1][n//2] = 1
    result[n//2][(n//2)+1] = 1
    result[(n//2)+1][(n//2)+1]
    result[(n//2)-1][n//2] = 1
    result[n//2][(n//2)-1] = 1
    return result

#3
def border(m,n):
    result = []
    for row in range(m):
        result.append([0]*n)
    for i in range(n):
        result[0][i] = 1
        result[m-1][i] = 1
    for i in range(m):
        result[i][0] = 1
        result[i][n-1] = 1
    return result

#4
def stripes(n):
    result = []
    for row in range(n):
        if row % 2 == 0:
            result.append([1]*n)
        elif row % 2 != 0:
            result.append([0]*n)
    return result