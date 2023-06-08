# Phone---Number

def main():
# Design and implementation


#  1.  Output a message to identify the program, and a blank line
    print("Breakdown of phone number to area code, prefix, line number")
    print()

#  2.  Input the 10-digit phone number
    Phone_number = int(input('Enter Phone Number: '))

#  3.  Breakdown the phone number
    area_code = Phone_number//10000000
    prefix = Phone_number%1000
    line_number = Phone_number%10000
    print()
    
   #  4. Output breakdown to area code, prefix, line number
    print('Phone number converted to area code=', area_code, ',prefix=', prefix, ',line number=', line_number)
    print()

main()
#end of program file
#The syntax error was due to a wrong quotation mark being used (‘ instead of ')
#SyntaxError: invalid character in identifier
#print(phone_str = ‘ (%s) %s-%s ’ % (area_code, prefix, line_number)
#I fixed the error by replacing the wrong quotation mark with the correct one (' instead of ‘).
#The semantics error was due to the fact that phone_number was an integer, but in the code it was being treated as a string, which caused an error when trying to index the string.
#Line 13 was where the error was.
#I fixed the error by converting phone_number to a string before breaking it down into area code, prefix, and line number.8886504343
