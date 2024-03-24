#1
#takes input of integers between 1 and 100 inclusive
def passing_1(li):
    result = 0
    for i in range(len(li)):
        if li[i] >= 60:
            result += 1
    return result

#2
#takes input of integers between 1 and 100 inclusive
def passing_2(li):
    result = []
    for i in range(len(li)):
        if li[i] >= 60:
            result.append(li[i])
    return result