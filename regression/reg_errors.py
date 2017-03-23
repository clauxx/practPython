from numpy import array
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib import style
import random

style.use('fivethirtyeight')

#xs = array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
#ys = array([x + x % 2 for x in xs])

def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return array(xs), array(ys)

xs, ys = create_dataset(40,40,2,correlation='pos')

def mean(x):
    summ = 0
    for i in x:
        summ += i
    return summ / len(x)


def slope_intercept(xs,ys):
    m = (mean(xs) * mean(ys) - mean(xs * ys)) / (mean(xs)**2 - mean(xs**2))
    b = mean(ys) - m * mean(xs)
    return m,b


m,b = slope_intercept(xs,ys)

def predict_y(x):
    yp = m * x + b
    return yp

def RSS(xs,ys):
    errs = []
    for x in range(len(xs)):
        yp = predict_y(xs[x])
        sqr_err = (ys[x] - yp)**2
        errs.append(sqr_err)
    return sum(errs)

def RSE(xs,ys):
    errs = RSS(xs,ys)
    return sqrt((1/(len(xs)-2)) * errs)

def TSS(ys):
    errs = []
    for y in ys:
        diff = (y - mean(ys)) ** 2
        errs.append(diff)
    return sum(errs)
        
def R_sq(xs,ys):
    rss = RSS(xs,ys)
    tss = TSS(ys)
    return 1 - (rss / tss)

def correlation(xs,ys):
    denom = []
    nom_1 = []
    nom_2 = []
    for i in range(len(xs)):
        x_diff = xs[i] - mean(xs)
        y_diff = ys[i] - mean(ys)
        denom.append(x_diff * y_diff)
        nom_1.append(x_diff ** 2)
        nom_2.append(y_diff ** 2)

    nom = sqrt(sum(nom_1)) * sqrt(sum(nom_2))
    return sum(denom) / nom
    

reg_line = [predict_y(x) for x in xs]

plt.scatter(xs,ys)
plt.plot(xs, reg_line, color='r')
plt.text(0,100, 'correlation: %s' % correlation(xs,ys))
plt.show()

print('correlation: ', correlation(xs,ys))
print('r^2: ', R_sq(xs,ys))
print('RSE: ', RSE(xs,ys))
print('RSS: ', RSS(xs,ys))
