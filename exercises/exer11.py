# 2D KEYPAD
keypad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for keys in keypad:
    for key in keys:
        print(key,end = " ")
    print()