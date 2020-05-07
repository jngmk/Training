import sys
sys.setrecursionlimit(15000)

class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}
        self.children_num = 0


class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.reverse_head = Node(None)
        self.count = 0

    def insert(self, string):
        cur_node = self.head
        cur_node.children_num += 1
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
            cur_node.children_num += 1

        cur_node.data = string
        cur_node.children_num += 1
        cur_node = self.reverse_head
        string = string[::-1]
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
            cur_node.children_num += 1

        cur_node.data = string

    def search(self, order, string):
        self.count = 0
        if order == 0:
            cur_node = self.head
        else:
            cur_node = self.reverse_head

        self._search(0, string, cur_node)
        return self.count

    def _search(self, k, string, cur_node):
        char = string[k]
        if char == '?':
            print(cur_node.children_num)
            self.count += cur_node.children_num
            return
        else:
            if char in cur_node.children:
                self._search(k+1, string, cur_node.children[char])


def solution(words, queries):
    answer = []
    trie_dict = dict()

    for word in words:
        length = len(word)
        if not trie_dict.get(length):
            trie_dict[length] = Trie()
        trie = trie_dict[length]
        trie.insert(word)

    for query in queries:
        print('query', query)
        cnt = 0
        length = len(query)
        if not trie_dict.get(length):
            answer.append(cnt)
            continue
        trie = trie_dict[length]

        if query[0] != '?' or (query[0] == '?' and query[-1] == '?'):
            cnt += trie.search(0, query)
        else:
            cnt += trie.search(1, query[::-1])
        answer.append(cnt)
    return answer


data = [
    [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "?????", "fr???", "fro???", "pro?"]],
]

for words, queries in data:
    print(solution(words, queries))
    break