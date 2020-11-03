
x = float(input("nhap x: "))
n = int(input("nhap n: "))


def x_mu_n(x, n):
    if (n == 0):
        return 1
    return x * x_mu_n(x, n - 1)


print("{} ^ {} = {}".format(x, n, x_mu_n(x, n)))
