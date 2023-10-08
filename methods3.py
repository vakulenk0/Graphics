import math
from decimal import *
def erf(x):
    x1 = 2/math.pi
    sum = 0.0
    for i in range(pow(10, 2)):
        if (i%2 == 0):
            sum+=(pow(x, 2*i+1))/(math.factorial(i)*(2*i+1))
        else:
            sum+=(-1*pow(x, 2*i+1))/(math.factorial(i)*(2*i+1))
    return x1*sum

def gauss_method(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        for k in range(i + 1, n):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
            vector[k] += c * vector[i]

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = vector[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            vector[k] -= matrix[k][i] * x[i]
    return x

#1
# A = [
#         [1.00, 0.80, 0.64],
#         [1.00, 0.90, 0.81],
#         [1.00, 1.10, 1.21]
#        ]
#
# erf08 = erf(0.8)
# # print(erf08)
# erf09 = erf(0.9)
# # print(erf09)
# erf11 = erf(1.1)
# # print(erf11)
# erf10 = erf(1.0)
# b = [erf08, erf09, erf11]
# print("Число обусловленности функции f(x) по отношению к аргументу x измеряет, насколько может измениться значение функции при небольшом изменении аргумента.")
# result = gauss_method(A, b)
# print("Решение системы уравнений:", result)
# print("sum: " + str(sum(result)))
# print("erf(1.0): " + str(erf10))



#2

# A = [
#     [0.1,0.2,0.3],
#     [0.4,0.5,0.6],
#     [0.7,0.8,0.9]
#      ]
# print("Если домножить первую строку на -2 и прибавить ко второй и домножить первую на -3 и прибавить к третьей, то получим, что 2 и 3 строки пропорциональны")
# print("x2 = 2*x1, где x1 - любой коэффициент из R", "            x3 = (-x1 - 2*x2)/3")
#
# b = [0.1,0.3,0.5]
#
# print("Пример решения: " + str(gauss_method(A,b)))