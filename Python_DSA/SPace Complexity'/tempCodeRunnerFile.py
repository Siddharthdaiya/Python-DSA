def sum(n):
    if n<=0:
        return n
    return n+sum(n-1)
sum(3)