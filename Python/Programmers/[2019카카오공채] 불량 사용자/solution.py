class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.result = []

    def insert(self, string, i):
        cur_node = self.head

        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)

            cur_node = cur_node.children[char]

        cur_node.data = i

    def search(self, string):
        cur_node = self.head
        self.result = []
        self._search(0, cur_node, string)
        return self.result

    def _search(self, k, cur_node, string):
        if k == len(string):
            if cur_node.data is not None:
                self.result.append(cur_node.data)
            return
        else:
            char = string[k]
            if char in cur_node.children:
                self._search(k+1, cur_node.children[char], string)
            elif char == '*':
                for char in list(cur_node.children.keys()):
                    self._search(k + 1, cur_node.children[char], string)


class Answer(object):
    def __init__(self, arr):
        self.arr = arr
        self.comb = []

    def get_answer(self):
        self._get_answer(0, self.arr, [])
        return self.comb

    def _get_answer(self, k, arr, tmp):
        if k == len(arr):
            tmp = list(sorted(tmp))
            if tmp not in self.comb:
                self.comb.append(tmp)
            return
        else:
            items = arr[k]
            for item in items:
                if item in tmp: continue
                self._get_answer(k+1, arr, tmp + [item])


def solution(user_id, banned_id):
    answer = []
    comb = []
    trie = Trie()
    for i in range(len(user_id)):
        user = user_id[i]
        trie.insert(user, i)

    for banned in banned_id:
        comb += [trie.search(banned)]

    answer = Answer(comb).get_answer()
    return len(answer)


dataset = [
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]],
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]],
    [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]]
]

for user_id, banned_id in dataset:
    print(solution(user_id, banned_id))
    # break