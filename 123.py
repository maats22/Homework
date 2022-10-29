print("Hi")
a=100
import math
x = float(input())
eps = float(input(1))
a = x
s = 0
i = 1
while abs(a) >= eps:

    s += a
    i += 1
    a *= (-1)*x*x// ((2*i - 2)*(2*i - 1))

print(s)
print(math.sin(x))
print(i - 1)