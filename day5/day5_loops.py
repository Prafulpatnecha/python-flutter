
# for Loop
print("for Loop-------------------------------------------------------")

for i in range(0,6):
    print(i)


# while Loop
print("while Loop-------------------------------------------------------")

i = 0

while i <= 5 :
    print(i)
    i+=1

# break and continue
print("break and continue-------------------------------------------------------")
for i in range(0,6) :
    if i==1:
        continue
    elif 5==i:
        break
    print(i)

# break and continue
print("Loop with Lists-------------------------------------------------------")

names = ["praful","prem","om"]

for list in names:
    print("Name : ",list)