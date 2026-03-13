from tree import *
import matplotlib.pyplot as plt
import random

#Helper functions
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

#Experiment code
    
def experiment1_1():
    length = 10000
    max = 10000
    runs = 1000

    average_difference = 0
    total = 0

    for _ in range(runs):
        values = create_random_list(length, max)
        Tree1 = RBTree()
        Tree2 = BSTree()
        for value in values:
            Tree1.insert(value)
            Tree2.insert(value)
        total += Tree2.get_height() - Tree1.get_height() 
    average_difference += total / runs

    print("Number of Nodes = " + str(length))
    print("Average Difference (BSTree Height - RBTree Height) = " + str(average_difference))

def experiment1_2():
    lengths = [1,2,4,8,16,32,64,128,256]
    max = 10000

    data_RBT = []
    data_BST = []

    for length in lengths:
        total_RBT = 0
        total_BST = 0

        for _ in range(1000):
            values = create_random_list(length, max)
            Tree1 = RBTree()
            Tree2 = BSTree()
            for value in values:
                Tree1.insert(value)
                Tree2.insert(value)
            total_RBT += Tree1.get_height()
            total_BST += Tree2.get_height()
        data_RBT.append(total_RBT/1000)
        data_BST.append(total_BST/1000)

    print("lengths = " + str(lengths))
    print("RBTree results = " + str(data_RBT))
    print("BSTree results = " + str(data_BST))

    plt.plot(lengths, data_RBT, color='red')
    plt.plot(lengths, data_BST, color='green')

    plt.xlabel('Number of Nodes')
    plt.ylabel('Average Height')
    plt.legend(['RBTree', 'BSTree'])
    plt.show()

def experiment2():
    swaps = [0,1,2,3,4,5,10,25,50,100]
    length = 50
    max = 10000
    runs = 1000

    data = []

    for num_swaps in swaps:
        total_diff = 0
        for _ in range(runs):
            values = create_near_sorted_list(length, max, num_swaps)
            Tree1 = RBTree()
            Tree2 = BSTree()
            for value in values:
                Tree1.insert(value)
                Tree2.insert(value)
            total_diff += Tree2.get_height() - Tree1.get_height() 
        data.append(total_diff / runs)

    print("swaps = " + str(swaps))
    print("results = " + str(data))


    plt.plot(swaps, data, color='red')

    plt.xlabel('Number of Swaps on a Sorted List')
    plt.ylabel('Average Difference in Height (BST Height - RBT Height)' )
    plt.show()

def experiment3():
    degrees = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    data = []

    for degree in degrees:
        data.append(XC3Tree(degree).get_height())

    print("heights: ", str(data))

    plt.plot(degrees, data, color='red')
    plt.xlabel('Degree')
    plt.ylabel('Height')
    plt.show()
#formula: h(i) = 1 + h(i-2)

def experiment4():
    degrees = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    data = []

    for degree in degrees:
        data.append(XC3Tree(degree).get_num_nodes())

    print("num_nodes: ", str(data))

    plt.plot(degrees, data, color='red')
    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes')
    plt.show()
#formula:

experiment1_1()





# tree = XC3Tree(5)
# print("Height: ", tree.get_height())
# print("Nodes: ", tree.get_num_nodes())






