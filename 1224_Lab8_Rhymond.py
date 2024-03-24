#1
def is_regular_d(di): 
  ans= len(di[0])
  for k,v in di.items():
    x= len(v)
    if x!= ans:
      return False
  return True

#2 
def is_regular_m(mat):
  x= mat[0].count(1)
  for row in mat:
    if row.count(1)!= x:
      return False
  return True