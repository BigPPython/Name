# Code: 1
# Create a program that takes a string name input, 
# and prints the name right after.
# Make sure to include a salutation.
import sys

a = '''**********************************
*WHAT IS YOUR SEXUAL ORIENTATION?*
*TYPE                            *
*M FOR MALE                      *
*F FOR FEMALE                    *
**********************************''' 
print(a) # prints string a
sex = str(input()) # user input
s =''
if sex in ['M', 'm']: # Conditional statement for question above
    s = 'Mr.'
elif sex in ['F', 'f']:
    b = '''    ******************
    *ARE YOU MARRIED?*
    *TYPE            *
    *YES OR NO       *
    ******************'''
    print(b)
    m = str(input())
    if m in ['y', 'Y', 'yes', 'Yes', 'YES']: # accepts all yes like answer
        s = 'Mrs '
    elif m in ['n', 'N', 'no', 'No', 'NO']: # accepts all no like answers
        s = 'Ms '
    else:
        print("PLEASE TRY AGAIN")
        sys.exit()
else:
    print("PLEASE TRY AGAIN")
    sys.exit()
    
print('Insert name here:')
name = str(input())
print('Hello, '+ s + name) # prints final result
sys.exit()
