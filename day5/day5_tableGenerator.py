
# Table With Input Generator App
print("----- Table Generator -----")
numTable = int(input("Enter a number : "))

print("Multiplication Table of ",numTable)

for i in range(1,11):
    print(numTable , "x" , i , "=" , numTable*i)