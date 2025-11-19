print("="*50)
print("             Enhances Student Grade Tracker    ")
print("="*50)

student_id= False
while not student_id:
    student_id= input("Enter ID: ")

    if student_id.startswith("-") and student_id [1:].isdigit():
        print("Please Enter Positive Number Only")
    elif student_id.isdigit():
        student_id=int(student_id)
        if student_id >0:
        student_id= True
        else:
          print("Zero Not Allowed")
else:
  print("Enter Number Only") 



