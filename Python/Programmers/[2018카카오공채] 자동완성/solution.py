class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.children_num = 0


class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.type_num = 0

    def insert(self, string):
        cur_node = self.head

        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
            cur_node.children_num += 1
            # print(cur_node.key, cur_node.children_num)

        cur_node.data = string

    def search(self, string):
        self.type_num = 0
        self._search(self.head.children[string[0]], string, 1)
        return self.type_num

    def _search(self, cur_node, string, k):
        if k == len(string):
            self.type_num += k
            return
        next_char = string[k]
        # print(next_char, k, cur_node.key, cur_node.children_num)
        if cur_node.children_num == 1:
            self.type_num += k
            return
        else:
            self._search(cur_node.children[next_char], string, k+1)


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.search(word)
        # print(word, answer)
    return answer


dataset = [
    ['go','gone','guild'],
    ['abc','def','ghi','jklm'],
    ['word','war','warrior','world'],
]

for words in dataset:
    print(solution(words))
    # break
