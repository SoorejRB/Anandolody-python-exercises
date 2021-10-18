# Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
  row = []
  for j in range(cols):
    row.append(0)
  matrix.append(row)

print(matrix)   