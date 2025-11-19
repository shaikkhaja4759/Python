import random
actual_otp = random.randint(1000,9999)
print(f"OTP Generate sent to Mobile {actual_otp}")
attempts=3
while attempts >0:
    print(f"You have {attempts} Left")
    user_otp = int(input("Enter the OTP: "))
    if len(str(user_otp)) !=4:
        print("OTP Must be 4 Digits")
        attempts -=1
        continue
    if user_otp == actual_otp:
        print("Correct OTP - Transaction Sucess")
        break
    else:
        print("Incorrect OTP")
        attempts -=1
else:
    print("Maximum Attempts Reached, Try after 24 hrs " )

    
