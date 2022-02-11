# Assignment 2.1
# Write a program that uses a print statement to say 'hello world' as shown in 'Desired Output'.
print("hello world")

# Assignment 2.2
# Write a program that uses input to prompt a user for their name and then welcomes them. 
# Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.
name = input("Enter your name")
print("Hello " + name)

# Assignment 2.3 
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to 
# test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

pay = float(hrs) * float(rate)
print("Pay: " + str(pay))

# Assignment 3.1
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate per hour:")
r = float(rate)

if h == 40:
    pay = h * r
    print('Pay: ' + str(pay))
else:
    pay = (40 * r) + (h -40) * (r * 1.5)
    print ('Pay: ' + str(pay))
