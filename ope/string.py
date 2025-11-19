Email =input("Enter the Email ID :")
formated_email=Email.lower()
print("orginal Email: " +Email)
print("orginal formated email: " +formated_email+"@gmail.com")


#pan = input("Enter the PAN ID: ")
#if pan.isalnum():
 #   format_pan = pan.upper()
#  print("orginal PAN: "+pan)
 #   print("format_pan: "+format_pan)
#else:
 #   Print("PAN is invalid")


mobile_number = input('Enter phone number with ISD CODE: ')
if mobile_number.startswith("+91"):
    print("Calling India Number charged in Rupees")
elif mobile_number.startswith("+1"):
    print("Calling USA Number charged in Dollers")
elif mobile_number.startswith("+33"):
    print("Calling France Number charged in Euros")
else:
    print("Calling supported to only India, USA & France Number")



emp_data = "Nihal,ganesh@gmail.com,25,Hyderabad,Developer"
formated = emp_data.split(",")
print ("Gmail :"+formated [1])
print ("Age: "+formated[-5])









