#!/usr/bin/python3

import random


def tree_generator(height, maximum):
    return pom_tree_generator(height, True, maximum)


def pom_tree_generator(h, root, maximum):
    h -= 1
    if 0 <= h:
        my_node = Node(random.randint(0, 100))
        if root:
            possibilities = random.randint(1, maximum)
            concrete = random.randint(0, possibilities - 1)
            for x in range(possibilities):
                if concrete == x:
                    my_node.adding(pom_tree_generator(h, True, maximum))
                else:
                    my_node.adding(pom_tree_generator(h, False, maximum))
        else:
            if random.randint(0, 1) == 1:
                possibilities = random.randint(1, maximum)
                for x in range(possibilities):
                    my_node.adding(pom_tree_generator(h, False, maximum))
        return my_node


    else:
        return None


class Node:
    def __init__(self, value):
        self.value = value
        self.sub_node = []

    def adding(self, node):
        if node is not None:
            self.sub_node.append(node)

    def bfs_pom_generator(self, h):
        if h > 0:
            for x in self.sub_node:
                for y in x.bfs_pom_generator((h - 1)):
                    yield y
        else:
            yield self.value

    def bfs_generator(self):
        a = 0
        b = True
        while b:
            b = False
            for x in self.bfs_pom_generator(a):
                b = True
                yield x
            a += 1

    def __repr__(self):
        return "% s " % self.value

    def dfs_generator(self):
        yield self.value
        for x in self.sub_node:
            for y in x.dfs_generator():
                yield y


if __name__ == "__main__":
    tree = tree_generator(4, 3)
    t = list(tree.dfs_generator())
    print(t)
    j = list(tree.bfs_generator())
    print(j)


