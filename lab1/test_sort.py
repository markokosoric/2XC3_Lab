from copy import deepcopy
from bad_sorts import create_random_list
from good_sorts import mergesort;


def test(sort):
    error = False;
    for i in range(100):
        for _j in range(100):
            L = create_random_list(i, 20000);
            L1 = deepcopy(L);
            L2 = deepcopy(L);
            sort(L1);
            mergesort(L2);
            if (L1 != L2):
                print("Failed test")
                print(L);
                print("");
                error = True
    if not error:
        print("test: success")
    else:
        print("failed tests")

