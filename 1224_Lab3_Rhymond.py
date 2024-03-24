#1
def neg_mul_5(li):
    result = []
    for i in range(len(li)):
        if li[i] % 5 == 0 and li[i] < 0:
            result.append(li[i])
    return result

#2
def neg_mul_5_while(li):
    result = []
    i = 0
    while i < len(li):
        if li[i] % 5 == 0 and li[i] < 0:
            result.append(li[i])
        i += 1
    return result