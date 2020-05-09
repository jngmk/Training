import sys
sys.setrecursionlimit(100000)


class Node(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.head = Node(None)
        self.pre_order = []
        self.post_order = []

    def insert(self, key, value):
        cur_node = self.head
        if cur_node.key is None:
            cur_node.key = key
            cur_node.value = value
        else:
            self._insert(cur_node, key, value)

    def _insert(self, cur_node, key, value):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(key, value)
                return
            else:
                self._insert(cur_node.left, key, value)
        else:
            if cur_node.right is None:
                cur_node.right = Node(key, value)
                return
            else:
                self._insert(cur_node.right, key, value)

    def preorder(self):
        self._preorder(self.head)
        return self.pre_order

    def _preorder(self, cur_node):
        self.pre_order.append(cur_node.key)
        if cur_node.left:
            self._preorder(cur_node.left)
        if cur_node.right:
            self._preorder(cur_node.right)

    def postorder(self):
        self._postorder(self.head)
        return self.post_order

    def _postorder(self, cur_node):
        if cur_node.left:
            self._postorder(cur_node.left)
        if cur_node.right:
            self._postorder(cur_node.right)
        self.post_order.append(cur_node.key)


def solution(nodeinfo):
    answer = []
    tree = Tree()
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(reverse=True, key=lambda x: x[1])
    for node in nodeinfo:
        tree.insert(node[2], node[0])
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    return answer


dataset = [
    [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],
]

for nodeinfo in dataset:
    print(solution(nodeinfo))