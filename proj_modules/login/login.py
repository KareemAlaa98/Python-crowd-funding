from proj_modules.projects import projects
def login():
    while True:
        login_email = input("enter your email: ")
        login_passwd = input("enter your password: ")
        file = open("users_log.txt", "r")
        for line in file:
            if line.startswith(login_email) and line.endswith(f'{login_passwd}\n'):
                print("Welcome, log in successful")
                user_projects_file = open(f'{login_email}.txt',"a")
                projects.projects(login_email)
        
        print("Wrong Email or Password")
        login()            
