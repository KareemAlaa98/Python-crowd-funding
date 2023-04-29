from proj_modules.registrations import register
from proj_modules.login import login

def crowdfund():
    input_option = input('Select Option Number: \n [1] Login \n [2] Register \n [3] Exit \n')

    if input_option == '1':
        login.login()

    elif input_option == '2': 
        register.register()
        crowdfund()

    elif input_option == '3':
        exit()
    else:
        print('You have not chosen a valid option')
        crowdfund()       

crowdfund()    

    