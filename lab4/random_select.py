import numpy as np
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('ff', help="first file name")
parser.add_argument('sf', help="second file name")
parser.add_argument('p', help="probability")
args = parser.parse_args()

def choose_rand_array(a, b, p):
    l1 = (np.random.random(len(a)))
    l1 = l1 > p
    return np.choose(l1, [b, a])


def where_rand_array(a, b, p):
    return np.where(np.random.random(len(a)) > p, a, b)

def arrays_reader(file1, file2, probability):
    in1 = open(file1, "r")
    in2 = open(file2, "r")
    a = np.array(((in1.readline()).replace("\n", "")).split(' '))
    b = np.array(((in2.readline()).replace("\n", "")).split(' '))
    in1.close()
    in2.close()
    return a, b, float(probability)


if __name__ == "__main__":
    a, b, p = arrays_reader(args.ff, args.sf, args.p)
    print('Where : ', where_rand_array(a, b, p))
    print('Choose : ', choose_rand_array(a, b, p))