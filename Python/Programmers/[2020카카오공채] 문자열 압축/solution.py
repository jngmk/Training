def solution(s):
    length = len(s)
    answer = length
    for i in range(1, (length//2)+1):
        before_word = ''
        sentence = ''
        count = 1
        for j in range(0, length, i):
            cur_word = s[j:j+i]
            if before_word == cur_word:
                count += 1
            else:
                if count != 1:
                    sentence += str(count)
                    count = 1
                before_word = cur_word
                sentence += before_word
        if count != 1:
            sentence += str(count)
        answer = min(answer, len(sentence))
    return answer


print(solution('abcabcabcabcdededededede'))