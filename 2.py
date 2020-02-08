import re

# Function to check username
def checkusername(u_name):
    len_uname = len(u_name)
    check_uppercase_user = re.findall(r'[A-Z]',u_name)
    check_specialchar_user = re.findall("[!,@,#,$,%,^,&,*,(,),_,-,+,<,>,?,/,{,}]",u_name)
    check_number_user =  re.findall("[0-9]", u_name)
    min_uname = int(5)
    max_uname = int(9)

    if len_uname < min_uname:
        print("\nWarning!!! Username is too short. Character minimum is 5 and character maximum is 9")
    elif len_uname > max_uname:
        print("\nWarning!!! Username is too long. Character minimum is 5 and character maximum is 9")
    elif (check_uppercase_user):
        print("\nWarning!!! The upper case is not allowed in username",check_uppercase_user)
    elif (check_specialchar_user):
        print("\nWarning!!! The special character is not allowed in username ",check_specialchar_user)
    elif (check_number_user):
        print("\nWarning!!! The number is not allowed in username",check_number_user)
    else:
        print("\nSuccess! Username is good")

# Function to check password
def checkpassword(password):
    len_password = len(password)
    min_char_password = int(8)

    check_uppercase_pass = re.findall("[A-Z]",password)
    check_specialchar_pass = re.findall("[!,@,#,$,%,^,&,*,(,),_,-,+]",password)
    check_number_pass =  re.findall("[0-9]", password)

    if len_password < min_char_password:
        print("\nWarning!!! Password is too weak. The password has to greater than 8 character or minimum 8 character")

    if (check_uppercase_pass and check_number_pass and check_specialchar_pass):
        print("Success! Password is good")
    else:
        print("\nWarning!!! Password must have at least one character uppercahse, one number and one special character")


# Main program
u_name = str(input("Username\t:"))
password = str(input("Password\t:"))

checkusername(u_name)
checkpassword(password)
