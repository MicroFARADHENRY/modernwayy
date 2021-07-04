print("Hello World")
print("Please enter a product price to begin")


p_r1=input("Enter Product price:")
p_r2=input("Enter Product price:")
p_r3=input("Enter Product price:")
p_r4=input("Enter Product price:")
result=float(p_r1)+float(p_r2)+float(p_r3)+float(p_r4)
print("Total Equals:")
print(result)
print("thank you for choosing us")
print("How about some guessing games?")
print("Guess the number 1 through 10")
enter_number=input("Enter a Number:")
if enter_number == '7':
    print("WooHoo")
else:
    print("Incorrect Number")
    print(" Try Again two attempts remaining")
    enter_number=input("Enter another Number:")
if enter_number == '7':
        print("congrats")
else:
    enter_number=input("Try One Last Time:")
    if enter_number == '7':
        print("Yay finally")
    else:
        print("Sorry Maybe Next time")

print("Shall we continue?")
yo_lo=input("YES or NO?:")
if yo_lo== 'YES':
    print("Okay Great!")
else:
    print("Okay comeback next time")

    input('Press ENTER to exit')
