import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Adding matrices
C = np.add(A, B)
print("Result:\n", C)
D = np.subtract(A, B)
print("Result:\n", D)
