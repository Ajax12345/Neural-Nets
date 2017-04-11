import random
from math import e

class Brain:
    def __init__(self, x, y):
        self.r = pow(10, -2) #learning rate
        self.threshold = pow(10, -3)
        self.k = 0#iteration index
        self.k_max = pow(10, 5)
        self.x = x
        self.y = y
        self.w = 0.01

    def begin_process(self):
        while self.k < self.k_max:
            self.random_selection
            self.k += 1

    def random_selection(self):
        self.key = random.randint(0, len(self.x))
        self.input = self.x[self.key]
        self.ouput = self.y[self.key]
        self.sums = sum([self.w*i for i in self.x])
        self.output = self.sigma(self.sums)
        self.sensitivity_l = 2*(self.output - self.y)
        self.sensitivity = self.sigma(self.sensitivity_l)*(1-self.sigma(self.sensitivity_l))*self.w*self.sensitivity_l
        self.g = self.sigma(self.sums)*self.sensitivity_l
        self.w -= self.r*self.g


    def sigma(self, z):
        return 1/(1+e**-z)

    def new_input(self, x):

        self.sums = sum([self.w*i for i in x])
        self.output = self.sigma(self.sums)
        print self.output




the_file = open("prediction_data.txt").readlines()

the_file = [i.strip('\n') for i in the_file]
data_file = [i.split() for i in the_file]

inputs = [map(float, i[:len(i)-1]) for i in data_file]
outputs = [i[len(i)-1] for i in data_file]
outputs = map(int, outputs)





the_brain = Brain(inputs, outputs)

the_brain.begin_process()
the_brain.new_input([1, 0])
