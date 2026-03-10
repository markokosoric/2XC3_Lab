from typing import Literal, Optional


class RBNode:
    value: int
    left: Optional[RBNode]
    right: Optional[RBNode]
    parent: Optional[RBNode]
    color: Literal["R", "B"]

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        if self.parent == None:
            raise Exception("parent is none")
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent == None:
            raise Exception("parent is none")
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        if self.parent == None:
            raise Exception("parent is none")
        return self.parent.get_brother()

    def uncle_is_black(self):
        u = self.get_uncle();
        if u == None:
            return True
        return u.is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        p = self.parent;
        l = self.left;
        assert l != None;
        v = l.right;

        if v != None:
            v.parent = self;
        l.right = self;
        l.parent = p;
        self.left = v;
        self.parent = l;
        if p != None:
            if p.left == self:
                p.left = l;
            else:
                p.right = l;


    def rotate_left(self):
        p = self.parent;
        r = self.right;
        assert r != None;
        v = r.left;

        if v != None:
            v.parent = self;
        r.left = self;
        r.parent = p;
        self.right = v;
        self.parent = r;
        if p != None:
            if p.left == self:
                p.left = r;
            else:
                p.right = r;



class RBTree:
    root: Optional[RBNode]

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            raise Exception("Not Implemented")
            #TODO

        if self.root == None:
            raise Exception("root is none")
        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
