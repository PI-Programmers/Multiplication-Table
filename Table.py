print("Multiplication Table")
print("            ")
n = int(input("Enter A Number : "))
print("            ")
m = int(input("Enter The Number Till you Want The Table: "))

o = m + 1
print("            ")
print("Multiplication Table Of" , n ," Multiplied Till" , m)

for i in range(1, o):
    
    print("            ")
    print(n, "X" , i , "=" , n * i)
