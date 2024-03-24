#1
def bubble_sort_for(li):
    i = 0
    while i < len(li)-1:
        j = 0
        while j < len(li)-i-1:
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
            j += 1
        i += 1