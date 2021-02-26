import big_o
from time import sleep
from tqdm import tqdm
from memory_profiler import profile



# for _ in range(10):
# arr_2[logn] ae


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

if __name__ == '__main__':
    exercise_7(3)