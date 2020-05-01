count = 0

def solution(words, queries):
    answer = []
    tree = dict()
    reverse_tree = dict()
    for word in words:
        now = tree
        reverse_now = reverse_tree
        for i in range(len(word)):
            # print('now', now)
            char = word[i]
            reverse_char = word[len(word)-i-1]
            # print('char', char)
            idx = ord(char) - 97
            reverse_idx = ord(reverse_char) - 97
            # print('idx', idx)
            if not now.get(idx):
                # print('##')
                now[idx] = {}
            # print('after', now)
            now = now[idx]
            if not reverse_now.get(reverse_idx):
                # print('##')
                reverse_now[reverse_idx] = {}
            # print('after', now)
            reverse_now = reverse_now[reverse_idx]

        now[26] = '.'
        reverse_now[26] = '.'
    # print(tree)

    prev_value = 0
    for query in queries:
        if answer:
            prev_value += answer[-1]
        if query[0] == '?':
            find(query[::-1], reverse_tree, 0)
        else:
            find(query, tree, 0)
        answer.append(count - prev_value)

    return answer


def find(query, now, k):
    global count
    if now == '.': return
    if k == len(query):
        if now.get(26):
            count += 1
        return
    else:
        char = query[k]
        if char != '?':
            idx = ord(char) - 97
            if now.get(idx):
                find(query, now[idx], k+1)
        else:
            for key in now.keys():
                # print(key)
                find(query, now[key], k+1)

data = [
    [["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]],
]

for words, queries in data:
    print(solution(words, queries))
    break
