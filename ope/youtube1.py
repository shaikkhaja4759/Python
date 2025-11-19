while True:
    num=int(input("Enter the Number: "))
    if num<=1:
        print("it is not a prime number")
    else:
        for i in range(2,num):
            if num % i==0:
                print("it is not a prime number")
                break
        else:
            print("Prime Number")
    choice=input("Do you want to enter the another number? (yes/no): ")
    if choice =="no":
        print("Program Stopped")
        break













