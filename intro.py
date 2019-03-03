import numpy

# Tutorial 3
def NN(m1, m2, w1, w2, b):
    z = m1*w1 + m2*w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+1+numpy.exp(-1))

w1 = numpy.random.randn()
w2 = numpy.random.randn()
b  = numpy.random.randn()

flower = NN(3, 1.5, w1, w2, b)
# print(flower)

# Tutorial 4
def cost(b):
    return (b - 4) ** 2

def num_slope(b):
    h = 0.0001
    return (cost(b + h) - cost(b)) / h

def slope(b):
    return 2 * (b - 4)

b = 8


for i in range(12000):
    b = b - .1 * slope(b)
    print(b)
#
# print(cost(3))
# print(num_slope(3))
# print(slope(3))