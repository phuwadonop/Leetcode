def length_of_longest_substring(s) :
    w_size = 0
    temp = []
    i = 0
    while i + w_size < len(s) :
        for j in range(i,len(s),1) :
            if s[j] in temp : break
            temp.append(s[j])
            if j-i >= w_size : w_size += 1
        temp.clear()
        i += 1
    return w_size
        

s = "dvdf"
print(length_of_longest_substring(s))