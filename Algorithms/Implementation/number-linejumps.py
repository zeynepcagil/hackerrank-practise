def kangaroo(x1, v1, x2, v2):
    if (v1 <= v2 and x1 < x2) or (v1 == v2 and x1 != x2):
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"