#1
def star_d(n):
    result = {}
    for row in range(n):
        result[row] = []
    for i in range(n-1):
        result[0].append(i+1)
    return result

#2
def star_m(n):
    result = []
    for row in range(n):
        result.append([0]*n)
    for i in range(n):
        result[0][i] = 1
    for i in range(n):
        result [i][0] = 1
    result[0][0] = 0
    return result

#3
def transpose_m(mat):
    result = []
    for row in range(len(mat)):
        result.append([0]*len(mat[row]))
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            result[col][row] = mat[row][col]
    return result

#4
def transpose_d(di):
    result = {}
    for row in range(len(di)):
        result[row] = []
    for k,v in di.items():
        for i in v:
            result[i].append(k)
    return result