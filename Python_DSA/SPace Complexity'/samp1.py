def sum(n):
    if n<=0:
        return n
    return n+sum(n-1)
sum(3)
# def f1(n):
#     if n <= 0:
#         return 1
#     else:
#         return 1 + f1(n-1)
# f1(3)