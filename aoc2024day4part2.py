import numpy as np

def isXmas(string1: str) -> bool:
    if(string1 == 'MMASS' or string1 == 'SSAMM'):
        return True
    elif (string1 == 'SMASM' or string1 == 'MSAMS'):
        return True
    else:
        return False

def constructDiagonal(num1,num2, matrix) ->str:
    testList = []
    testList.append(matrix[num1-1,num2-1])#topleft
    testList.append(matrix[num1 + 1, num2 - 1])#bottomright
    testList.append(matrix[num1, num2]) #middle
    testList.append(matrix[num1 - 1, num2 + 1]) #topright
    testList.append(matrix[num1 + 1, num2 + 1]) #bottomright
    return "".join(testList)

with open("input4.txt", "r") as file:
    lines = file.readlines()

matrix = []

for line in lines:
    matrix.append(list(line)[:140])




rows = len(matrix)
cols = len(matrix[0])

# print(rows)
# print(cols)

matrix_np = np.array(matrix)
total=0



#check all diagonal right

for i in range(1, rows-1):
    for j in range(1, cols-1):
        if isXmas(constructDiagonal(i,j,matrix_np)):
            total+=1





print(total)




