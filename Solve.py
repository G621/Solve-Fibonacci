# Matrix multiplication
def matrix_multiply(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
    return c


# Matrix power
def matrix_pow(a, n):
    ret = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            ret = matrix_multiply(ret, a)
        n >>= 1
        a = matrix_multiply(a, a)
    return ret


# Calculate the nth term of Fibonacci number
def fib(n):
    if n < 2:
        return n

    q = [[1, 1], [1, 0]]
    res = matrix_pow(q, n - 1)
    return res[0][0]