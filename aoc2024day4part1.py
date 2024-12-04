import numpy as np

def isXmas(string1: str) -> bool:
    if(string1 == 'XMAS' or string1 == 'SAMX'):
        return True
    else:
        return False

def constructLeftDiagonal(num1,num2, matrix) ->str:
    testList = []
    row=num1
    while num1< row+4:
        testList.append(matrix[num1,num2])
        num1+=1
        num2+=1
    return "".join(testList)
def constructRightDiagonal(num1,num2, matrix) ->str:
    testList = []
    row=num1
    while num1< row+4:
        testList.append(matrix[num1,num2])
        num1+=1
        num2-=1
    return "".join(testList)



with open("input4.txt", "r") as file:
    lines = file.readlines()

matrix = []

for line in lines:
    matrix.append(list(line)[:140])




rows = len(matrix)
cols = len(matrix[0])

print(rows)
print(cols)

matrix_np = np.array(matrix)
total=0

print(constructRightDiagonal(0,9,matrix_np))
for row in range(rows):
    l=0
    r=4
    while(r< cols+1):
        window = "".join(matrix_np[row,l:r])
        if(isXmas(window)):
            total+=1
        r+=1
        l+=1

print(f"total found in rows : {total}")


for col in range(cols):
    t=0
    b=4
    while b< rows+1:
        window = "".join(matrix_np[t:b,col])


        if isXmas(window):
            total += 1
        t += 1
        b += 1


#check all diagonal right

for i in range(rows-3):
    for j in range(cols-3):
        if isXmas(constructLeftDiagonal(i,j,matrix_np)):
            total+=1

for i in range(rows-3):
    for j in range(cols-1,2,-1):
        if isXmas(constructRightDiagonal(i,j,matrix_np)):
            total+=1
        if(i==0 and j==0 ):
            print(constructRightDiagonal(i,j,matrix_np))



print(total)




