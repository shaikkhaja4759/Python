while True:
    name=input("Enter the customer Name: ")
    total=0

    while True:
        print("Enter the amount and quantity")
        amount=float(input("Enter the Amount:"))
        quantity=int(input("Enter the Quantity: "))
        total+=amount*quantity
        repeat=input("Do you want add more items? (yes/no): ")
        if repeat=="no" or repeat=="No":
            break
    print("Thanks")
    print("Amount to be paid: ",total)

 




    



        





    