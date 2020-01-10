import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)

            cur_node = cur_node.children[char]

        cur_node.data = string

    def search(self, string):
        cur_node = self.head

        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False

            if cur_node.data is not None:
                return True


T = int(input())
for _ in range(T):
    N = int(input())
    trie = Trie()
    consistency = True
    tels = []
    for _ in range(N):
        tels.append(input().strip())
    tels = list(sorted(tels))
    for tel in tels:
        if trie.search(tel):
            consistency = False; break
        else:
            trie.insert(tel)

    print('YES' if consistency else 'NO')
