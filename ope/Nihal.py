if 5> 2:
    print(" yes thats correct")



#name = input("Enter Your Name: ")
#print("Welcome "+name)

#age =int(input("Enter Your Age: "))
#f age>=18:
#   print("You can Vote")
#lse:
 #  print("You can't vote")


   #age=int(input("Enter your Age: "))
   #status="you can vote" if age>=18 else "You cannot vote"
   #print(status)
    
   #marks=int(input("Enter your Marks: "))
   #if marks>=90:
    #   print("A")
    #lif marks>=75:
   #    print("B")
   #elif marks>= 65:
   #    print("C")
   #else:
    #   print("Failed")


#ge=int(input("Enter your age: "))
#f age>=18:
 #  has_id=input("Do You have id(yes/no): ")
  # if has_id =="yes":
   # print("You can Vote")
   #else:
   #
   # print("You need an id to vote")inp

Student_name =input("Enter Your Name: ")
Student_grade =int(input("Enter Grade Level: "))
Basic_Tution_fee=1000
Discount=0
Actual_Fee=0
if Student_grade>= 9 and Student_grade<=12:
        print("10% Discount")
        Discount=Basic_Tution_fee*0.1
elif Student_grade>=6 and Student_grade<=8:
     print("5% Discont")
     Discount=Basic_Tution_fee*0.05
else:
    print("Appropriate error message for invalid grades")

Actual_Fee =Basic_Tution_fee - Discount
print(Actual_Fee)

print(f"student Name {Student_name},Grade{Student_grade},Tution Fee{Basic_Tution_fee},Discount{Discount},Actual Fee{Actual_Fee}")

      
      



















