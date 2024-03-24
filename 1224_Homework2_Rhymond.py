#1
def foo_for(n):
    count = 10
    for i in range(7, (2 * n + 2)+1, 3):
        count += i
    return count

#2
#n is an integer greater than 1
def identity(n):
    result = []
    for row in range(n):
        result.append([0]*n)
    for i in range(n):
        result[i][i] += 1
    return result

#3
#n is an integer greater than 1
def anti_identity(n):
    result = []
    for row in range(n):
        result.append([0]*n)
    for i in range(n):
        result[i][n-1] += 1
        n -= 1
    return result

#4
#n is an integer greater than 2
def zee(n):
    result = []
    for row in range(n):
        result.append([0]*n)
    for i in range(n):
        result[0][i] = 1
        result[n-1][i] = 1
        for i in range(n):
            result[i][n-1] = 1
            n -= 1
    result[len(result)-1][i] = 1
    return result

#5
#m and n are both integers greater than 2
def edges(m,n):
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
