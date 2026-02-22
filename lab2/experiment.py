import graph
import matplotlib.pyplot as plt
import timeit
import gc
import time
import sys


def check_pred(p, i, j) -> bool:
    g = graph.create_random_graph(i,j);
    return p(g)

def check_prob(p, i, j, n) -> float:
    count = 0;
    for k in range(n):
        count += int(check_pred(p,i,j));
    return float(count)/n;

def produce_results(p, nodes, edges, runs) -> list[int]:
    res = [];
    for i in edges:
        res.append(check_prob(p, nodes, i, runs));
    return res;


def experiment1():
    nodes = 100;
    edges = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, ];

    res = produce_results(graph.has_cycle, nodes, edges, 100);

    print("edges = " + str(edges))
    print("results = " + str(res))

    plt.plot(edges, res, color='red');

    plt.xlabel('edges')
    plt.ylabel('probability of a cycle')
    plt.show()

def experiment2():
    nodes = 100;
    edges = [ 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, ];

    res = produce_results(graph.is_connected, nodes, edges, 100);

    print("edges = " + str(edges))
    print("results = " + str(res))

    plt.plot(edges, res, color='red');

    plt.xlabel('edges')
    plt.ylabel('probability of connected')
    plt.show()


def experiment_approximations_1():
    nodes = 8
    edges = [1, 5, 10, 15, 20, 25, 28]
    runs = 1000
    data_a1 = []
    data_a2 = []
    data_a3 = []

    for num_of_edges in edges:
        total_MVC, total_a1, total_a2, total_a3 = 0, 0, 0, 0
        for i in range(runs):
            G1 = graph.create_random_graph(nodes, num_of_edges)
            
            total_MVC += len(graph.MVC(G1))
            total_a1 += len(graph.approx1(G1))
            total_a2 += len(graph.approx2(G1))
            total_a3 += len(graph.approx3(G1))

        data_a1.append(total_a1 / total_MVC)
        data_a2.append(total_a2 / total_MVC)
        data_a3.append(total_a3 / total_MVC)

    print("edges = " + str(edges))
    print("approximation 1 results = " + str(data_a1))
    print("approximation 2 results = " + str(data_a2))
    print("approximation 3 results = " + str(data_a3))

    plt.plot(edges, data_a1, color='red')
    plt.plot(edges, data_a2, color='green')
    plt.plot(edges, data_a3, color='blue')

    plt.xlabel('edges')
    plt.ylabel('Expected Approximation Ratio')
    plt.legend(['approx1', 'approx2', 'approx3'])
    plt.show()

def experiment_approximations_2():
    nodes = [4,5,6,7,8]
    edges = 5
    runs = 1000

    data_a1 = []
    data_a2 = []
    data_a3 = []

    for num_of_nodes in nodes:
        total_MVC, total_a1, total_a2, total_a3 = 0, 0, 0, 0
        for i in range(runs):
            G1 = graph.create_random_graph(num_of_nodes, edges)
            
            total_MVC += len(graph.MVC(G1))
            total_a1 += len(graph.approx1(G1))
            total_a2 += len(graph.approx2(G1))
            total_a3 += len(graph.approx3(G1))

        data_a1.append(total_a1 / total_MVC)
        data_a2.append(total_a2 / total_MVC)
        data_a3.append(total_a3 / total_MVC)

    print("nodes = " + str(nodes))
    print("approximation 1 results = " + str(data_a1))
    print("approximation 2 results = " + str(data_a2))
    print("approximation 3 results = " + str(data_a3))

    plt.plot(nodes, data_a1, color='red')
    plt.plot(nodes, data_a2, color='green')
    plt.plot(nodes, data_a3, color='blue')

    plt.xlabel('nodes')
    plt.ylabel('Expected Approximation Ratio')
    plt.legend(['approx1', 'approx2', 'approx3'])
    plt.show()

def experiment_approximations_3():
    nodes = 5
    runs = 100
    num_of_edges = [1,2,3,4,5,6,7,8,9,10]
    edges = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    powerset_of_edges = graph.power_set(edges)
    print(powerset_of_edges)

    data_a1 = []
    data_a2 = []
    data_a3 = []

    for i in num_of_edges:
        worst_a1, worst_a2, worst_a3 = 0, 0, 0
        for edge_set in powerset_of_edges:
            if len(edge_set) == i:
                total_MVC = 0
                G1 = graph.Graph(nodes)
                
                for edge in edge_set:
                    G1.add_edge(edge[0], edge[1])

                total_MVC = len(graph.MVC(G1))

                if total_MVC == 0:
                    continue

                worst_a1 = max(worst_a1, len(graph.approx1(G1)) / total_MVC)
                local_worst2 = 0
                local_worst3 = 0
                for _ in range(runs):
                    local_worst2 = max(local_worst2, len(graph.approx2(G1)) / total_MVC)
                    local_worst3 = max(local_worst3, len(graph.approx3(G1)) / total_MVC)

                worst_a2 = max(worst_a2, local_worst2)
                worst_a3 = max(worst_a3, local_worst3)  

        data_a1.append(worst_a1)
        data_a2.append(worst_a2)
        data_a3.append(worst_a3)

    print("edges = " + str(num_of_edges))
    print("approximation 1 results = " + str(data_a1))
    print("approximation 2 results = " + str(data_a2))
    print("approximation 3 results = " + str(data_a3))

    plt.plot(num_of_edges, data_a1, color='red')
    plt.plot(num_of_edges, data_a2, color='green')
    plt.plot(num_of_edges, data_a3, color='blue')

    plt.xlabel('edges')
    plt.ylabel('Worst-Case Approximation Ratio')
    plt.legend(['approx1', 'approx2', 'approx3'])
    plt.show()

def experiment_MIS_MVC_correlation():
    nodes = 10;
    edges = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            48,
            49,
            50,
            51,
            52,
            53,
            54,
            ]
    runs = 1000;

    avg_indep = [];
    avg_vertc = [];

    for e in edges:
        indep = 0;
        vertc = 0;
        for _ in range(runs):
            g = graph.create_random_graph(nodes, e);
            indep += len(graph.mis(g));
            vertc += len(graph.MVC(g));
        avg_indep.append(float(indep)/float(runs));
        avg_vertc.append(float(vertc)/float(runs));

    print("edges = " + str(edges));
    print("avg_indep = " + str(avg_indep));
    print("avg_vertc = " + str(avg_vertc));
    plt.plot(edges, avg_indep, color='red')
    plt.plot(edges, avg_vertc, color='blue')
    plt.xlabel('edges')
    plt.ylabel('avg')
    plt.legend(['independent set size', 'vertex cover size'])
    plt.show()

def experiment_MIS_MVC_correlation_process_data():
    f = open("./experiment_MIS_MVC_correlation_output.txt")
    d = {};
    exec(f.read(), {}, d) # make sure `experiment_mis_output.txt` has not been tampered with before running
    edges = d['edges'];
    new_data = [];
    for i in range(len(edges)):
        new_data.append(d['avg_indep'][i] + d['avg_vertc'][i]);
    plt.plot(edges, new_data, color='green')
    plt.plot(edges, d['avg_indep'], color='red')
    plt.plot(edges, d['avg_vertc'], color='blue')
    plt.xlabel('edges')
    plt.legend(['sum', 'independent set size', 'vertex cover size'])
    plt.show()

experiment_approximations_3()