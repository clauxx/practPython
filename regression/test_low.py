import matplotlib.pyplot as plt
from numpy import array

xs = array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
ys = array([x + ((x) % 4) for x in xs])

def mean(x):
    summ = 0
    for i in x:
        summ += i
    return summ / len(x)

def slope_interc(xs,ys):
    m = (mean(xs) * mean(ys) - mean(xs * ys)) / (mean(xs) ** 2 - mean(xs ** 2))
    b = mean(ys) - (m * mean(xs))
    return m,b

m,b = slope_interc(xs,ys)

plt.scatter(xs,ys, color='b')
plt.plot(xs, m*xs+b, color='r')
plt.show()


