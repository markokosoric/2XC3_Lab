import math

class MinHeap:
    length: int = 0
    data: list[Element] = []
    map: dict[int, int]

    def __init__(self, L: list[Element]):
        self.data = L
        self.length = len(L)
        self.map = {}
        for i in range(len(L)):
            self.map[L[i].value] = i
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i: int):
        smallest_known = i
        if self.left(i) < self.length and self.data[self.left(i)].key < self.data[i].key:
            smallest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)].key < self.data[smallest_known].key:
            smallest_known = self.right(i)
        if smallest_known != i:
            self.data[i], self.data[smallest_known] = self.data[smallest_known], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[smallest_known].value] = smallest_known
            self.sink(smallest_known)

    def insert(self, element: Element):
        if len(self.data) == self.length:
            self.data.append(element)
        else:
            self.data[self.length] = element
        self.map[element.value] = self.length
        self.length += 1
        self.swim(self.length - 1)

    def insert_elements(self, L: list[Element]):
        for element in L:
            self.insert(element)

    def swim(self, i: int):
        while i > 0 and self.data[i].key < self.data[self.parent(i)].key:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[self.parent(i)].value] = self.parent(i)
            i = self.parent(i)

    def get_min(self) -> Element:
        if len(self.data) > 0:
            return self.data[0]
        raise Exception("tried to get min on size 0 minheap")

    def extract_min(self) -> Element:
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.map[self.data[self.length - 1].value] = self.length - 1
        self.map[self.data[0].value] = 0
        min_element = self.data[self.length - 1]
        self.length -= 1
        self.map.pop(min_element.value)
        self.sink(0)
        return min_element

    def decrease_key(self, value: int, new_key: float):
        if new_key >= self.data[self.map[value]].key:
            return
        index = self.map[value]
        self.data[index].key = new_key
        self.swim(index)

    def get_element_from_value(self, value: int) -> Element:
        return self.data[self.map[value]]

    def is_empty(self) -> bool:
        return self.length == 0

    def left(self, i: int) -> int:
        return 2 * (i + 1) - 1

    def right(self, i: int) -> int:
        return 2 * (i + 1)

    def parent(self, i: int) -> int:
        return (i + 1) // 2 - 1

    def __str__(self) -> str:
        height: int = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height + height
        s: str = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

class Element:
    value: int
    key: float

    def __init__(self, value: int, key: float):
        self.value = value
        self.key = key

    def __str__(self) -> str:
        return "(" + str(self.value) + "," + str(self.key) + ")"

# nodes1 = [Element("A", 5), Element("B", 1), Element("C", 10), Element("D", 2), Element("E", -3)]
nodes2 = [Element(1, 1), Element(2, 1), Element(3, 10), Element(4, 2), Element(5, -3)]
