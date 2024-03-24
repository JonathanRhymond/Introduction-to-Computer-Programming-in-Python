#1
def swap(li):
    small = li[0]
    for i in li:
        if i < small:
            small = i
    x = li[0]
    li[li.index(small)] = x
    li[0] = small
    return li