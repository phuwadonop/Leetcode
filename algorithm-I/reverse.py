def reverse_string(str) :
    l = 0
    r = len(str) - 1
    while (l < r) : 
        temp = str[l]
        str[l] = str[r]
        str[r] = temp
        l += 1
        r -= 1
def reverse_string_2(s) :
    for i in range(len(s)) :
        s[i] , s[-1-i] = s[-1-i], s[i]

s = ["h","e","l","l","o"]
reverse_string_2(s)
print(s)