# pip install big-O
import big_o


def exercise_2(n):
    a, b = 0, 0
    if a < n:
        while a < n:
            a += 1
            b += 1
    else:
        while a < 10:
            a += 1
            b += 1
    return b


print("N1 ", big_o.big_o(exercise_2, big_o.datagen.n_, max_n=100000, n_repeats=100)[0])


def exercise_3(n):
    a, b = 10, 0
    for i in range(a):
        while n > 0:
            n -= 1
            b += 1
    return b


print("N2 ", big_o.big_o(exercise_3, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])


def exercise_5(n):
    a, c = 10, 0
    while a > 0:
        for i in range(a):
            b = 1
            while b < n:
                n -= 1
                c += 1
        a -= 1
    return c


print("N3 ", big_o.big_o(exercise_5, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])


def exercise_7(n):
    a, c = 0, 0
    while a < n:
        for i in range(a):
            b = 1
            while b < n:
                b += 1
                c += 1
        a += 1
    return c


print("N4 ", big_o.big_o(exercise_7, big_o.datagen.n_, max_n=10, n_repeats=10)[0])


def exercise_9(n):
    a, c = 0, 0
    while a < n:
        b = 1
        while b < n:
            b += 1
            c += 1
        a += 2
    return c


# since, the time complexity of this algorithm is too high, to check it max_n and n_repeats was decreased to minimum
print("N5 ", big_o.big_o(exercise_9, big_o.datagen.n_, max_n=10, n_repeats=10)[0])


def exercise_10(n):
    a, c = 1, 0
    while a < n:
        b = 1
        while b < n:
            b += 1
            c += 1
        a *= 2
    return c


print("N6 ", big_o.big_o(exercise_10, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])


def exercise_13(n):
    a = 0
    arr = []
    while n > a:
        arr.append(n * a)
        a += 1
    return arr


print("N7 ", big_o.big_o(exercise_13, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])


def exercise_15(n):
    a = 0
    arr = []
    while a < 10:
        arr.append(n)
        b = 0
        while n > b:
            arr[-1] += 1
            b += 1
        a += 1
    return arr


print("N8 ", big_o.big_o(exercise_15, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])


def exercise_17(n):
    a = 0
    arr = []
    while n > a:
        b = 1
        while n > b:
            arr.append(n)
            b *= 2
        a += 2
    return arr


print("N9 ", big_o.big_o(exercise_17, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])


def exercise_18(n):
    a = 0
    arr_1 = []
    while n > a:
        b = 1
        arr_2 = []
        while n > b:
            arr_2.append(n)
            b *= 2
        arr_1.append(arr_2)
        a += 1
    return arr_1


print("N10 ", big_o.big_o(exercise_18, big_o.datagen.n_, max_n=1000, n_repeats=100)[0])

'''
Output we will get. 

N1  Linear: time = -0.00018 + 2.2E-05*n (sec) -
N2  Linear: time = -0.00023 + 5.6E-05*n (sec) -
N3  Linearithmic: time = 0.0026 + 6.4E-06*n*log(n) (sec) -
N4  Cubic: time = -0.0047 + 1.2E-06*n^3 (sec)
N5  Quadratic: time = -4.8E-05 + 1.3E-06*n^2 (sec)
N6  Linear: time = -0.011 + 0.00025*n (sec) -
N7  Linearithmic: time = 0.0023 + 6.7E-06*n*log(n) (sec) -
N8  Linearithmic: time = 0.012 + 7.2E-05*n*log(n) (sec) -
N9  Linearithmic: time = -0.0018 + 2.4E-05*n*log(n) (sec)
N10 Linearithmic: time = 0.007 + 5.1E-05*n*log(n) (sec)

N1  Logarithmic: time = -0.039 + 0.0086*log(n) (sec)
N2  Quadratic: time = 0.0052 + 5.8E-08*n^2 (sec)
N3  Logarithmic: time = -0.093 + 0.02*log(n) (sec)
N4  Cubic: time = -0.0094 + 1.2E-06*n^3 (sec)
N5  Linearithmic: time = -0.0013 + 2.5E-05*n*log(n) (sec)
N6  Linear: time = -0.012 + 0.00024*n (sec)
N7  Linearithmic: time = 0.0049 + 5.6E-06*n*log(n) (sec)
N8  Linear: time = -0.0018 + 0.00045*n (sec)
N9  Linearithmic: time = -0.0003 + 2.2E-05*n*log(n) (sec)
N10  Linearithmic: time = 0.0057 + 4.5E-05*n*log(n) (sec)

N1  Quadratic: time = 0.0052 + 1.9E-08*n^2 (sec)
N2  Linear: time = 0.00095 + 4.7E-05*n (sec)
N3  Linear: time = 0.003 + 4.1E-05*n (sec)
N4  Cubic: time = -0.013 + 1.2E-06*n^3 (sec)
N5  Quadratic: time = -0.00066 + 1.4E-06*n^2 (sec)
N6  Linear: time = -0.0041 + 0.00024*n (sec)
N7  Linear: time = -0.0023 + 7.1E-05*n (sec)
N8  Linear: time = 0.00094 + 0.00045*n (sec)
N9  Linearithmic: time = 0.0022 + 2E-05*n*log(n) (sec)
N10  Linear: time = -0.013 + 0.00032*n (sec)
'''