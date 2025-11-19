while True:
    num=int(input("Enter the number: "))
    if num <=1:
      print("it is not a prime number")
    else:
       for i in range(2,num):
           if num % i==0:
            print("it is not a prime number")
            break
       else:
          print("Prime number")
    choice=input("Do you want to check another number?(yes/no): ") 
    if choice =="no":
       print("program Stopped")
       break  

    

