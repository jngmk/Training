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

    def starts_with(self, prefix):
        cur_node = self.head
        subtrie = None

        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                subtrie = cur_node
            else:
                return False

        q = list(subtrie.children.values())

        if q: return True


T = int(input())
for _ in range(T):
    N = int(input())
    trie = Trie()
    consistency = True
    tels = []
    for _ in range(N):
        tels.append(int(input().strip()))
    tels = list(sorted(tels))
    for tel in tels:
        trie.insert(str(tel))

    for tel in tels:
        if trie.starts_with(str(tel)):
            consistency = False
            break

    print('YES' if consistency else 'NO')
