'''
This script will tell us whether a pariticular inputted email is valid or not. By Using different String methods.

1. An email should contain basic things like: 
    a. A very basic email contains atleast 6 characters in it. (ex: s@g.in)  
    b. First Character Should not be a digit- must start with a letter
    c. should not contain more than 1 '@' symbols.
    d. The dot should be present before 2 or 3 characters from the end.
    e. Email should not contain space in it. It should not have upper case letters in it. 
    f. It can have special characters like "_", "."

2. To acheive all these things we make use of different, different string functions with different operators.
'''

email = input("Enter a email to be checked: ") #s@g.in (6-characters minimum)

#These variables will be used later and based on these variables we will decide - whether email is valid or not.
space = False
upperCase = False
specialCharacters = False

if len(email) >= 6:
    if email[0].isalpha(): #isalpha() - checks whether a particular character is alphabet or not.
        if ("@" in email) and (email.count('@')==1): #Checking multiple Conditions for '@' and using membership operator to check if '@' is present in email or not
            if (email[-4]=='.') ^ (email[-3]=='.'): #using xor operator, it will ensure that at a time there wont be two dots. If there are 2 dots successively at a time then it will return False and go to else block
                for letter in email:# To traverse and check each and every letter
                    if letter==letter.isspace():
                        space = True 
                    elif letter.isalpha():
                        if letter==letter.upper():
                            upperCase = True
                    # these below 2 elif's are permissible so we are simply ignoring those letters
                    elif letter.isdigit():
                        continue
                    elif letter == '_' or letter == '.' or letter == '@':
                        continue
                    else: # This block is for any special characters like *,#,$,...
                        specialCharacters = True
                if space == True or specialCharacters == True or upperCase == True:
                    print("Invalid Email!!! Doesn't match the required things.(Avoid uppercase/space/specialcharacters )")
                else:
                    print("Valid Email!!! :)")

            else:
                print("Invalid Email!!! Dot is not at the correct position!")
        else:
            print("Invalid Email!!! Excessive '@' symbols!")
    else:
        print("Invalid Email!!! First Character should be letter only!")
else:
    print("Invalid Email!!! Length is too short!")