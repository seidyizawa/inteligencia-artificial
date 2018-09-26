import random
import math
LIMIT = 100000

def uptemp(T, k):
    return T - 0.001

def vizinhos(i, L):
    assert L > 1 and i >= 0 and i < L
    if i == 0:
        return [1]
    elif i == L - 1:
        return [L - 2]
    else:
        return [i - 1, i + 1]

def mover(x, A, T):
    nhb = random.choice(xrange(0, len(A)))

    delta = A[nhb] - A[x]

    if delta < 0:
        return nhb
    else:
        p = math.exp(-delta / T)
        return nhb if random.random() < p else x

def simulated_annealing(A):
    L = len(A)
    x0 = random.choice(xrange(0, L))
    T = 1.
    k = 1

    x = x0
    x_best = x0

    while T > 1e-3:
        x = mover(x, A, T)
        if(A[x] < A[x_best]):
            x_best = x
        T = uptemp(T, k)
        k += 1

    print ("iteracoes:", k)
    return x, x_best, x0

def isminima_local(p, A):
    return all(A[p] < A[i] for i in vizinhos(p, len(A)))

def func(x):
    return math.sin((2 * math.pi / LIMIT) * x) + 0.001 * random.random()

def initialize(L):
    return map(func, xrange(0, L))

def main():
    A = initialize(LIMIT)

    local_minima = []
    for i in xrange(0, LIMIT):
        if(isminima_local(i, A)):
            local_minima.append([i, A[i]])

    x = 0
    y = A[x]
    for xi, yi in enumerate(A):
        if yi < y:
            x = xi
            y = yi
    global_minumum = x

    print ("numeros de minimos locais: %d" % (len(local_minima)))
    print ("minimo global @%d = %0.3f" % (global_minumum, A[global_minumum]))

    x, x_best, x0 = simulated_annealing(A)
    print ("a solucao e  @%d = %0.3f" % (x, A[x]))
    print ("a melhor solucao e  @%d = %0.3f" % (x_best, A[x_best]))
    print ("a solucao de inicio e @%d = %0.3f" % (x0, A[x0]))
if __name__ == '__main__':
    main()
