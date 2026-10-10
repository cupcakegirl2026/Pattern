print("This is a half pyramid made of stars ")
row=int(input("Enter number of rows:"))

for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()
    