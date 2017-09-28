import math
import numpy as np
data = """
0 0 0
0 1 1
1 0 1
1 1 0
"""
#three hidden layers
def activate(x):
    return 1/float(1+pow(math.e, -1*x))

def sigmoid_prime(x):
    return pow(math.e, -1*x)*pow((1+pow(math.e, -1*x)), -2)

random_val = np.random.uniform(0, 0.9)
s = [map(int, b.split()) for b in data.split("\n") if b]
s1 = {tuple(i[:2]):i[-1] for i in s}

matrix_data = [{tuple(i[:2]):[[np.random.uniform(0, 0.99) for b in range(3)] for c in i[:2]]} for i in s]
layer_weights = [np.random.uniform(0, 0.99) for i in range(3)]
final_layer_weights = {a:[np.random.uniform(0, 0.99) for i in range(3)] for a in s1}


second = {d.keys()[0]:[[[c*a for c in b] for a, b in zip(val1, val2)] for val1, val2 in d.items()][0] for d in matrix_data}

third = {a:[c+d for c, d in zip(*b)] for a, b in second.items()}
fourth = {a:map(activate, b) for a, b in third.items()}
fifth = {a:sum(a*b for a, b in zip(fourth[a], final_layer_weights[a])) for a in fourth}

final_predictions = {a:activate(b) for a, b in fifth.items()}

print final_predictions
error_margin = {a:s1[a]-b for a, b in final_predictions.items()}
print "error margin", error_margin
backprop1 = {a:sigmoid_prime(fifth[a])*error_margin[a] for a in final_predictions}

print "backprop1", backprop1
