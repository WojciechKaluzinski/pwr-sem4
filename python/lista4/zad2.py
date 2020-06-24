#!/usr/bin/python3
import random
import collections


def tree_generator(h):
    t = 2 ** (h - 1)
    maximum = random.randint(1, t)

    return pom_tree_generator(0, h, maximum)


def pom_tree_generator(actual_h, h, maximum):
    actual_h += 1
    if actual_h < h:
        if maximum > 0:
            if 2 ** actual_h < maximum:
                l = pom_tree_generator(actual_h, h, 0)
                r = pom_tree_generator(actual_h, h, maximum)
                return [random.randint(0, 100), l, r]
            else:
                l = pom_tree_generator(actual_h, h, maximum)
                r = pom_tree_generator(actual_h, h, 0)
                return [random.randint(0, 100), l, r]
        if random.randint(0, 1) == 1:
            l = pom_tree_generator(actual_h, h, 0)
            r = pom_tree_generator(actual_h, h, 0)
            return [random.randint(0, 100), l, r]
        else:
            return None

    return [random.randint(0, 100), None, None]


def dfs_generator(it):
    for x in it:
        if x is not None:
            if (isinstance(x, collections.Iterable) and
                not isinstance(x, str)):
                for y in dfs_generator(x):
                    yield y
            else:
                yield x




def bfs_pom_generator(it, h):
    if h>0:
        for x in it:
            if type(x)==list:
                 for y in bfs_pom_generator(x,(h-1)):
                     yield y
    else:
        for x in it:
            if x is not None and type(x)!=list:
                yield x

def bfs_generator(it):
    a=0
    b = True
    while b:
         b = False
         for x in bfs_pom_generator(it,a):
             b=	True
             yield x
         a+=1

            

if __name__ == "__main__":
    tree = tree_generator(4)
    print(tree)
    print(list(dfs_generator(tree)))
    print(list(bfs_generator(tree)))




