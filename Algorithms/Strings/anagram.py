from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s)%2!=0:
        return -1
    else:
        mid= len(s)//2
        s1=s[:mid]
        s2=s[mid:]
        
        #Counter fonksiyonu içindeki her bir harfin kaç kere geçtiğini sayar.
        #Örnek:  Counter("aabbcc") => Counter({'a': 2, 'b': 2, 'c': 2})
 
        c1=Counter(s1)
        c2=Counter(s2)
        changes = 0
        for char in c1:
            if c1[char]> c2.get(char,0): #Bu harf, s1’de daha fazla varsa → demek ki fazla var, fazlaları değiştirmek gerek.
                changes+=c1[char]-c2.get(char,0) #s1’deki bu harften, s2’deki karşılık kadarını eşleştir, kalanını değiştirmek zorundasın.


        return changes  