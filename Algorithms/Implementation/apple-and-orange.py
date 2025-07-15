def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count=0
    orange_count=0
    
    for apple in apples:
        apple_position=a+apple
        if apple_position>=s and apple_position<=t:
            apple_count+=1
    for orange in oranges:
        orange_position=b+orange
        if orange_position<=t and orange_position>=s:
            orange_count+=1
    print(apple_count)
    print(orange_count)    