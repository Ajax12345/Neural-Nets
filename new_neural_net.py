import numpy as np
from random import randint

class Neural:
    def __init__(self, x, y):
        #self.w = np.random.rand(3, 3)
        self.x = x
        self.y = y
        #create w1 and w2


    def phi(self, x): #passing vector
        return 1/(1+np.exp(-x)) #carefull with float

    def gradient_descent(self):
        raise NotADirectoryError("Working on it")
        self.first_val = self.w



if __name__ == "__main__":
    f = open('data.txt').readlines()


    f = [map(int, i.strip('\n').split()) for i in f]

    X = [[1]+i[:2] for i in f]

    Y = [i[-1] for i in f]


    #* linear algebra mult (numpy: a.dot(b))
    #.* element-wise (numpy: a*b)
    newy = list(set(Y))

    many_to_one = {a:[1 if b == i else 0 for b in range(len(newy))] for i, a in enumerate(newy)}

    print many_to_one





    yprime = [many_to_one[i] for i in Y]
