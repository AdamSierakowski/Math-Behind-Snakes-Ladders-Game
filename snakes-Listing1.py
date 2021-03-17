from numpy.linalg import matrix_power
import numpy as np


def snakes_and_ladders_matrix():
    n = 101
    T = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(i + 1, np.min([n, i + 7])):
            T[i, j] = 1 / 6
    for i in range(n - 6, n):
        T[i, i] = (i - n + 7) / 6

    snakes_and_ladders = np.array([
        [98, 78],  [95, 75],  [93, 73],  [87, 24], [64, 60],
        [62, 19],  [56, 53],  [49, 11], [47, 26],  [16, 6],
        [1, 38],  [4, 14], [9, 31],  [21, 42], [28, 84],
        [36, 44], [51, 67],  [71, 91], [80, 100]])

    for src, dst in snakes_and_ladders:
        b = T[:, src].copy()
        T[:, dst] += b
        T[:, src] = 0
    return T


def main():
    T = snakes_and_ladders_matrix()
    Q = T[:-1, :-1]
    I = np.identity(100)
    o = np.ones((100, 1))

    # method 1
    result = np.linalg.solve(I - Q, o)
    print("via solve", result[0, 0])

    # method 2
    N = np.linalg.inv(I - Q)
    sum = np.sum(N, axis=1)
    print("via inver", sum[0])

    # method 3
    Napprx = np.zeros((100, 100))
    for k in range(1000):
        Napprx += matrix_power(Q, k)
    sumapprx = np.sum(Napprx, axis=1)
    print("via apprx", sumapprx[0])


main()
