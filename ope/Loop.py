for num in range(10):
    print(num)

for char in range(10):
    print("Hi")

for num in range(2,10,2):
    print(num)

for outer in range(1,5):
    for inner in range(1,5):
        print(f"outer {outer} * {inner} ={outer*inner}")
    
for outer in range(2,10):
    for  inner in range(2,10):
        print(f"outer {outer} * {inner} = {outer*inner}")


password = "login@123"
user_given_password =""
while user_given_password != password:
    user_given_password= input("Enter password:")
  print("Password Matched,Login Success")
