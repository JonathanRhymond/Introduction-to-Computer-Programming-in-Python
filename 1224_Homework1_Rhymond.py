#1
def seconds(min):
  return 60 * min

#2
import math
def sphere(r):
  return math.pi * 4/3 * (r ** 3)

#3
def widgets(num):
  if num <= 10:
    return 1.05 * (20 * num)
  if num > 10 & num < 20:
    return 1.05 * (18 * num)
  if num >= 20:
    return 1.05 * (16 * num)

#4
def every_other(li):
  nli = []
  i = 0
  while i < len(li):
    nli.append(li[i])
    i += 2
  return nli

#5
li = [4, 3, 7, 8, 9, 2, 1, 5, 6]
print(li[0:4])
print(li[2:5])
print(li[6:])
