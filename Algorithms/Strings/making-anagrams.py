def makingAnagrams(s1, s2):
    count_s1=Counter(s1)
    count_s2=Counter(s2)
    total_deletion=0
    for char in set(s1+s2):
        diff=abs(count_s1[char]-count_s2[char]) # abs mutlak değer
        total_deletion+=diff
    return total_deletion    