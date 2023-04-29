import re

def register():
    file = open('users_log.txt',"a")
    while True:
        fname = input('enter your first name: ')
        if re.match("^[A-Za-z]+$",fname):
            break
    while True:
        lname = input('enter your last name: ')
        if re.match("^[A-Za-z]+$",lname):
            break
    while True:
        email = input('enter your email: ')
        if re.match(r'^([a-z\d\.-]+)@([a-z\d-]+)\.(com)$', email):
        # check if email already exists
            file = open('users_log.txt')
            for line in file:
                while line.startswith(email):
                    print('email already exist please enter a diffrent email')
                    email = input('re-enter your email: ')    
            break
    while True:
        passwd = input('enter your password: ')
        confirm_passwd = input('confirm your password: ')
        if passwd == confirm_passwd:
            break
    while True:
        phone_num = input("enter your phone number: ")
        if phone_num.isdigit() and len(phone_num) == 11 and re.match("[0-9]",phone_num):
            if re.match("^010",phone_num) or re.match("^011",phone_num) or re.match("^015",phone_num) or re.match("^012",phone_num):
                break
        else:
            print("Please Enter a valid Egyptian number")    
    user = f"{email}:{fname}:{lname}:{phone_num}:{passwd}\n"
    # adding user        
    users_log= open('users_log.txt','a')
    users_log.write(user)
    users_log.close()
    print("user created")

