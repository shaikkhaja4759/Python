student_name="nihal"
student_age=30
student_cgpa=9.8
student_passed=True


print(student_name)
print(student_age)
print(student_cgpa)
print(student_passed)


#print("My name is " + student_name +" and my age after 5 years would be",student_age+5)

print("my name is {student_name} and my age is {student_age}")
print(f"my name is {student_name} and my age is {student_age}")
print(f"my name is {student_name} and my age is after 5 years{student_age+ 5}")

num1 =10
num2 =5
print(f"sum of {num1} and {num2} is {num1+num2}" )
print(f"Difference of{num1} and {num2} is {num1-num2}")
print(f"product of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")


a=3
b=2      
print (f"Floor Division of {a} and {b} is {a//b}")
print(f"Division of {a} and {b} is {a/b}")

print(f"Exponentiation Division of {a} and {b} is {a**b}")


TV = 1000000
Downpayment = 500000
Loan =500000
Anual_interest = 12
tenuer= 5
Months= 60

monthly_interest = Anual_interest / (12 *100)
Monthly= monthly_interest * 12

total_interest = Loan + Monthly 
total_Loan_interest = Loan + total_interest
EMI = total_Loan_interest/60




print(f" My Loan Amount {Loan}")
print(f" Total Interest {total_interest}")
print(f" Loan & Interest {total_Loan_interest}")
print(f" Tenuer {tenuer}")
print(f" Final EMI per month {EMI}")




x=10
x +=5
print(x)

count =1
count -= 1
print(count)

num1 =10
num2 =5
num3 =3
num4 =15


print(num1 ==num2)
print(num1 != num2)
print(num1 > num2)
print(num1 <num2)
print("=============")
result_not= num1>num2 or num3<num4
print(result_not)
print(not result_not)

print("========================")

data ="python is easy to learn"
find_word =" java"
found = find_word in data
print(found)

print("===============")

#data ="1001"
#print(dir(data))

n1=10
n2=5.5

sum=(n1+n2)

print(sum)

pi = 3.5
pi = int
print(pi)


rating="4"
print(type(rating))
rating += 1







