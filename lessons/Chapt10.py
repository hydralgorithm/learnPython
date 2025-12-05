# Nested loops

# EXAMPLE 1
# for x in range(3):
#     for y in range (1,10):
#         print(y,end=" ")
#     print()

# EXAMPLE 2
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter number of columns: "))
sym = input("Enter a symbol: ")
# x=0
# while not x == rows:
#     for y in range(0,cols):
#         print(f"{sym}",end=" ")
#     print()
#     x+=1
# OR
for x in range(rows):
    for y in range(cols):
        print(f"{sym}",end=" ")
    print()