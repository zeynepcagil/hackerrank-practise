def introTutorial(V, arr):
    for i,value in enumerate(arr):
        if value==V:
            return i
    return -1