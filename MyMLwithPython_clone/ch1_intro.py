import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n", x)
print(x.shape)
from scipy import sparse

eye = np.eye(4)
print("nympy eye array:\n", eye)
sparse_matrix = sparse.csr_matrix(eye)
print(sparse_matrix)

data = np.ones(4)
print(data)
col_indices = np.arange(4)
row_indices = np.arange(4)

coo_matrix = sparse.coo_matrix((data, (col_indices, row_indices)))
print(coo_matrix)

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker='x')
# plt.show()
from sklearn.datasets import load_iris

data = load_iris()
print(data.keys())
