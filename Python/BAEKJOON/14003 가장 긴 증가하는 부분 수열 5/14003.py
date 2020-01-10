class Node(object):
    def __init__(self, key, cnt=0):
        self.key = key
        self.order = cnt+1
        self.children = {}


class Tree(object):
    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def insert(self, value):
        cur_node = self.head
        self._insert(cur_node, value)

    def _insert(self, cur, v):
        if not cur.children:
            cur.children[v] = Node(v, cur.order)
            if self.length < cur.order + 1:
                self.length = cur.order+1

        else:
            for num in cur.children:
                if num < v:
                    self._insert(num, v)
                elif cur.children.get(v) is None and num > v:
                    cur.children[v] = Node(v, cur.order)


