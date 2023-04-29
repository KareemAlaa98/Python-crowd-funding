import re

def projects(login_email):
    proj_options = input('Select an option:\n [1] Create new project \n [2] View all projects \n [3] Delete project\n [4] Edit project\n [5] Exit\n')
    
    ## 1 create new project ##
    if proj_options == '1':
        create_projects(login_email)
        projects(login_email)

    ## 2 View all projects ##
    elif proj_options == '2':
        file = open('all_projects.txt')
        for line in file:
            print(f'{line}\n')
        print('what else would you like to do?')    
        projects(login_email)    


    # 3 delete project #
    elif proj_options == '3':
        deleteProject(login_email)
        projects(login_email)                       

    ## 4 edit project ##
    elif proj_options == '4':
            editProject(login_email)
            projects(login_email)


    ## 5 exit ##
    elif proj_options == '5':
        exit()
    else:
        print("You haven't selected a valid option")
        projects()



## create project function ## 
def create_projects(email):
    proj_title = input('enter project title: ')
    # check if project exists
    projects_file = open(f'{email}.txt', 'r')
    for line in projects_file:
        while proj_title in line:
            proj_title = input('you already have a project with this title, enter a new project title: ')

    proj_describtion = input("describe your project: ")

    proj_target = input("enter your projet's target: ")
    while not proj_target.isdigit():
        proj_target = input("enter your projet's target: ")

    proj_start_date =  input("enter projet's START date eg. 21/01/2023: ")
    check_date(proj_start_date)   
    proj_end_date =   input("enter projet's END date eg. 21/01/2023: ")
    check_date(proj_end_date)   

    usr_project = f"{proj_title}:{proj_describtion}:{proj_target}:{proj_start_date}:{proj_end_date}\n"

    projects_file = open(f'{email}.txt', 'a')
    projects_file.write(usr_project)
    projects_file.close
    all_projects_file = open('all_projects.txt', 'a')
    all_projects_file.write(usr_project)
    all_projects_file.close
    print('your project is created successfully.\n what else would you like to do?')


## check date format function ##
def check_date(date):
    while not re.match("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$",date):
        date = input("enter your date correctly in Day/Month/Year format: ")


## delete project fnction ##
def deleteProject(email):
    project_to_delete = input("Enter the project's name to delete: ")

    def check_Project_Exists(email, project_to_delete):
        file = open(f'{email}.txt')
        for line in file:
            if line.startswith(project_to_delete):
                return True
        return False
            
    if check_Project_Exists(email, project_to_delete):
        with open(f"{email}.txt", "r") as f:
            lines = f.readlines()
        with open(f"{email}.txt", "w") as f:
            for line in lines:
                line = line.rstrip()
                if not line.startswith(project_to_delete):
                    f.write(f'{line}\n')
        ## delete the project from the all projects file ##            
        with open("all_projects.txt", "r") as f:
            lines = f.readlines()
        with open("all_projects.txt", "w") as f:
            for line in lines:
                line = line.rstrip()
                if not line.startswith(project_to_delete):
                    f.write(f'{line}\n')            

    else:
        print("Project does not exist enter a valid name")
        deleteProject(email)

## edit projects function ##
def editProject(email):
    prompt = input("delete or create a project?")
    if prompt == "create":
        create_projects(email)
    elif prompt == "delete":    
        deleteProject(email)


    