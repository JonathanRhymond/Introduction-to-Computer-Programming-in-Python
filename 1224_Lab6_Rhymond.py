test_dict = {0 : [1, 2, 4], 1 : [0, 2, 3, 4, 5], 2 : [0, 1], 3 : [1, 4], 4 : [0, 1, 3], 5 : [1]}

test_mat = [[0, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0]]

#1
def min_degree_d(di):
  result = len(di.items())
  for k, v in di.items():
    if len(v) < result:
      result = len(v)
  return result

#2
def min_degree_m(mat):
  result = len(mat)
  for row in mat:
    if row.count(1) < result:
      result = row.count(1)
  return result

print(min_degree_d(test_dict))
print(min_degree_m(test_mat))