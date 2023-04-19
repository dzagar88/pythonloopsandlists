#Import random
import random
#Create the function below:
def matrixBuilder(number):
    matrix = []
    for i in range(number):
        row = []
        for j in range(number):
            row.append(1)
        matrix.append(row)
    return matrix
print(matrixBuilder(3))