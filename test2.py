from time import sleep

import big_o
from tqdm import tqdm


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


def exercise_3(n):
    a, b = 10, 0
    for i in range(a):
        while n > 0:
            n -= 1
            b += 1
    return b


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


def exercise_9(n):
    a, c = 0, 0
    while a < n:
        b = 1
        while b < n:
            b += 1
            c += 1
        a += 2
    return c


def exercise_10(n):
    a, c = 1, 0
    while a < n:
        b = 1
        while b < n:
            b += 1
            c += 1
        a *= 2
    return c


def check(func, type_of_complexity_to_check, number_of_repeats, min, max, repeats):
    counter = 0
    for _ in tqdm(range(0, number_of_repeats), desc=func.__name__):
        sleep(.1)
        if type(big_o.big_o(func, big_o.datagen.n_, min_n=min, max_n=max, n_repeats=repeats)[0]) == type_of_complexity_to_check:
            counter += 1
    return counter / number_of_repeats * 100


if __name__ == '__main__':
    '''wanted to use multithreading to run all algorithms in one time but, did not understand the whole idea of threds
    in python so to check it need spend litte bit more time'''
    print("\n percentage = ", check(exercise_2, big_o.complexities.Linear, 300,1,1000, 100), " % \n")
    # print("percentage = ", check(exercise_3, big_o.complexities.Linear, 300,1000, 100), " % \n")
    # print("percentage = ", check(exercise_5, big_o.complexities.Linear, 300, 1000, 100), " % \n")
    # print("percentage = ", check(exercise_9, big_o.complexities.Quadratic, 300, 10, 100), " % \n")
    # print("percentage = ", check(exercise_10, big_o.complexities.Linearithmic, 300, 1000, 100), " % \n")
