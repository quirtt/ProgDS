# # Fold with integral objective
# # Input: Delta^c, L, N
# import numpy as np
# from itertools import combinations

# # Define necessary functions or replace them with actual implementations
# def uniform_sample(N, c):

#     pass

# def fold(p, L, i, j):

#     pass

# # Input variables
# c = 10  # Define the value of c
# N = 100  # Define the value of N
# L = np.random.rand(c, c)  # Assuming L is a random matrix of shape (c, c)
# SN = 10  # Assuming SN is a constant value

# # Initialize matrix M with large initial distance
# M = np.zeros((c, c))
# M += 10**4

# # Generate uniform samples on the simplex
# P = uniform_sample(N, c)

# # Calculate values for matrix M
# for i, j in combinations(range(c), 2):
#     H_p = np.einsum("ac,bc->ba", L, P).min(axis=1)
#     q, Lt = fold(P, L, i, j)
#     H_q = np.einsum("ac,bc->ba", Lt, q).min(axis=1)
#     M[i, j] = (H_q - H_p).mean(axis=0)

# # Find indices of minimum value in matrix M
# i_fold, j_fold = np.unravel_index(np.argmin(M), M.shape)

# print("Minimum indices (i, j):", i_fold, j_fold)
import numpy as np
def generate_points_in_simplex(N, c):
    points = np.random.rand(N, c)
    points /= points.sum(axis=1)[:, None]
    return points

c = 5
M = np.zeros((c,c))
M = M + 10**4
p = generate_points_in_simplex(5, 4)
L = np.array([[1, 2], [3, 4]])
p = np.array([[5], [6]])
for i in range(c):
    for j in range(i+1, c):
        H_p = einsum("ac,cb->ab", L, p).min(axis = 0)
        q, Lt = fold(p, L, i, j)
# L is A x C, p is C x 1 -> Lp = A x 1