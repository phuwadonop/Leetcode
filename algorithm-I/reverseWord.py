def reverse_word(s):
    list = s.split(' ')
    string = ""
    for j in range(len(list)):
        for i in range(len(list[j])):
            string += list[j][-i - 1]
        if j != len(list) - 1:
            string += ' '
    return string


def reverse_word_2(s):
    s_list = s.split(' ')
    l = []
    for word in s_list:
        ls = list(word)
        ls.reverse()
        l.append(''.join(ls))
    return ' '.join(l)

def reverse_word_3(s):
    list = s.split(' ')
    string = ""
    for j in range(len(list)):
        string += list[j][::-1]
        if j != len(list) - 1:
            string += ' '
    return string



s = "Let's take LeetCode contest"
print(reverse_word_3(s))
