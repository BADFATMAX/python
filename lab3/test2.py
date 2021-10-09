import random

def creatArray():
    return [[random.randint(-100, 100) for i in range(3)] for j in range(3)]

matrix1 = creatArray()
matrix2 = creatArray()

with open('input.txt', 'w') as testfile:
    for row in matrix1:
        testfile.write(' '.join([str(a) for a in row]) + '\n')

with open('input2.txt', 'w') as testfile:
    for row in matrix2:
        testfile.write(' '.join([str(a) for a in row]) + '\n')

with open('input.txt', 'r') as f:
    ln = [[int(i) for i in line.strip().split()] for line in f]
print(ln)
with open('input2.txt', 'r') as f:
    lnn = [[int(i) for i in line.strip().split()] for line in f]
print(lnn)

result1 = [[0,0,0], [0,0,0], [0,0,0]]
result2 = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(ln)):
   for j in range(len(ln[0])):
              result1[i][j] = ln[i][j] + lnn[i][j]

for i in range(len(ln)):
   for j in range(len(ln[0])):
              result2[i][j] = ln[i][j] - lnn[i][j]


print("   ")
for r in result1:
      print(r)
print("   ")

for r in result2:
      print(r)

print(" ")
print("SUMMA=", sum(sum(result1, [])))
print("SUMMA=", sum(sum(result2, [])))