def isValid(s):
    counter_s=Counter(s)
    freq_counts = Counter(counter_s.values())
    if len(freq_counts)>2:
        return "NO"
    elif len(freq_counts)==2:
        f1,f2 = freq_counts.keys()
        c1,c2=freq_counts[f1],freq_counts[f2]
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"
        if abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
            return "YES"

        
        return "NO"    
    
    else:
        return "YES" 