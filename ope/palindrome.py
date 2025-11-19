while True:
    num=int(input("Enter the Number: "))
    reverse_num=int(str(num)[::-1])
    if num==reverse_num:
       print("Palindrome number")
    else:
      print("not a palindrome number")
      break
    
#
text=input("Enter the string: ")
if text.lower()==text [::-1]:
   print("Palindrome")
else:
   print("Not palindrome")
