# Star pattern printing using loops

rows = int(input("Enter number of rows: "))

print("\nStar Pattern:")

for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()
  

# Reverse triangle pattern

print("\nReverse Star Pattern:")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
