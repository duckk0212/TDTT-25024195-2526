def factory(n) -> int:
    giaithua = 1
    if n < 0:
        return False
    for i in range(1, n + 1):
        giaithua *= i
    return giaithua

n = int(input())
for x in range(1,n+1):
    if (factory(x)):
        print(x)