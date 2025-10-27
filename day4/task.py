# Number input lo aur check karo "Even" ya "Odd".

while True :
    num = int(input("Enter Any One Number To Find Even & Odd : "))

    # for i in num :
    if num%2==0:
        print("Even : ", num)
    else:
        print("Odd : ", num)