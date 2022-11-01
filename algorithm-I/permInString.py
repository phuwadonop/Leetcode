from collections import defaultdict


def check_inclusion(s1,s2) : # got TLE
    
    size = len(s1)
    start = 0
    
    while len(s2) - start >= size :
        temp = list(s1)
        for i in range(start,start+size,1) :
            if s2[i] in temp : temp.remove(s2[i])
        if len(temp) == 0 : return True
        start += 1
    return False 

def check_inclusion_2(s1,s2) : 
    
    d1 = defaultdict(int)
    for c in s1 : d1[c] += 1
    
    size = len(s1)
    start = 0
    
    while len(s2) - start >= size :
        d2_temp = defaultdict(int)
        temp = s2[start:start+size]
        for c in temp : d2_temp[c] += 1
        if d2_temp == d1 : return True
        start += 1
    return False 

def check_inclusion_3(s1,s2) : 
    
    d1 = defaultdict(int)
    for c in s1 : d1[c] += 1
    
    size = len(s1)
    start = 0
    
    d2 = defaultdict(int)
    print(d1)
    while len(s2) - start >= size :
        if start == 0 :
            temp = s2[start:start+size]
            for c in temp : d2[c] += 1
            print("start.." )
            print(d2)
        else : 
            d2[s2[start+size-1]] += 1
            print("increased " + str(s2[start+size-1]))
        if d2 == d1 : return True
        print("Before decrease " + str(s2[start]))
        print(d2)
        if d2[s2[start]] > 1 : d2[s2[start]] -= 1
        else : del d2[s2[start]]
        print("After decrease "  + str(s2[start]))
        print(d2)
        start += 1
    return False 

# d1 = defaultdict(int)
# d2 = defaultdict(int)
# s = 'sd'
# for c in s : d2[c] += 1
# for c in s : d1[c] += 1

s1 , s2 = "ab","eidbaooo"
print(check_inclusion_3(s1,s2))