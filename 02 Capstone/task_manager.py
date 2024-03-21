# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Define functions
def reg_user():
    '''Add a new user to the user.txt file'''

    while True:
        new_username = input("New Username: ")

        # Check if the username already exists
        if new_username in username_password.keys():
            print("Username already exists. Please choose a different username.")
            continue

        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")

        if new_password == confirm_password:
            print("New user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
            break
        else:
            print("Passwords do not match")


def add_task():
    '''Allow a user to add a new task to task.txt file'''

    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    '''Reads the tasks from tasks.txt file and prints to the console'''

    for idx, t in enumerate(task_list, start=1):
        disp_str = f"Task Number: {idx}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine():
    '''View tasks assigned to the current user'''

    print("Your Tasks:")
    for idx, t in enumerate(task_list, start=1):
        if t['username'] == curr_user:
            disp_str = f"Task Number: {idx}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Completed: \t {t['completed']}\n"
            print(disp_str)

    while True:
        task_choice = input("Enter the number of the task you want to select or -1 to return to the main menu: ")
        if task_choice == "-1":
            break
        elif not task_choice.isdigit():
            print("Invalid input. Please enter a number or -1.")
            continue

        task_index = int(task_choice) - 1
        if task_index < 0 or task_index >= len(task_list):
            print("Invalid task number. Please enter a valid task number or -1 to return to the main menu.")
            continue

        selected_task = task_list[task_index]
        print("Selected Task:")
        disp_str = f"Task: \t\t {selected_task['title']}\n"
        disp_str += f"Assigned to: \t {selected_task['username']}\n"
        disp_str += f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {selected_task['description']}\n"
        disp_str += f"Completed: \t {selected_task['completed']}\n"
        print(disp_str)

        edit_choice = input("Enter 'm' to mark the task as complete or 'e' to edit the task: ")
        if edit_choice == 'm':
            selected_task['completed'] = True
            print("Task marked as complete.")
        elif edit_choice == 'e':
            if not selected_task['completed']:
                new_username = input("Enter the new username or press Enter to keep the current one: ")
                if new_username != "":
                    selected_task['username'] = new_username

                new_due_date = input("Enter the new due date (YYYY-MM-DD) or press Enter to keep the current one: ")
                if new_due_date != "":
                    try:
                        selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                    except ValueError:
                        print("Invalid date format. Task due date not changed.")
            else:
                print("Completed tasks cannot be edited.")


def generate_reports():
    '''Generate reports'''
    # Check if the reports already exist
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        print("Reports not found. Generating reports...")
        # Generate reports if they don't exist
        total_tasks = len(task_list)
        if total_tasks == 0:
            print("No tasks found. Exiting report generation.")
            return

        completed_tasks = sum(1 for task in task_list if task['completed'])
        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < date.today())

        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100

        task_overview = "Task Overview:\n\n"
        task_overview += "Total Number of Tasks: {}\n".format(total_tasks)
        task_overview += "Total Number of Completed Tasks: {}\n".format(completed_tasks)
        task_overview += "Total Number of Uncompleted Tasks: {}\n".format(uncompleted_tasks)
        task_overview += "Total Number of Overdue Tasks: {}\n".format(overdue_tasks)
        task_overview += "Percentage of Tasks Incomplete: {:.2f}%\n".format(incomplete_percentage)
        task_overview += "Percentage of Tasks Overdue: {:.2f}%\n\n".format(overdue_percentage)

        total_users = len(username_password.keys())
        user_overview = "User Overview:\n\n"
        user_overview += "Total Number of Users: {}\n".format(total_users)
        user_overview += "Total Number of Tasks: {}\n\n".format(total_tasks)

        for user, password in username_password.items():
            user_tasks = [task for task in task_list if task['username'] == user]
            total_user_tasks = len(user_tasks)
            completed_user_tasks = sum(1 for task in user_tasks if task['completed'])
            uncompleted_user_tasks = total_user_tasks - completed_user_tasks
            overdue_user_tasks = sum(1 for task in user_tasks if not task['completed'] and task['due_date'].date() < date.today())

            user_task_percentage = (total_user_tasks / total_tasks) * 100
            completed_user_percentage = (completed_user_tasks / total_user_tasks) * 100
            uncompleted_user_percentage = (uncompleted_user_tasks / total_user_tasks) * 100
            overdue_user_percentage = (overdue_user_tasks / total_user_tasks) * 100

            user_overview += "User: {}\n".format(user)
            user_overview += "Total Number of Tasks Assigned: {}\n".format(total_user_tasks)
            user_overview += "Percentage of Total Tasks Assigned: {:.2f}%\n".format(user_task_percentage)
            user_overview += "Percentage of Completed Tasks: {:.2f}%\n".format(completed_user_percentage)
            user_overview += "Percentage of Uncompleted Tasks: {:.2f}%\n".format(uncompleted_user_percentage)
            user_overview += "Percentage of Overdue Tasks: {:.2f}%\n\n".format(overdue_user_percentage)

        # Write to files
        with open("task_overview.txt", "w") as task_file:
            task_file.write(task_overview)

        with open("user_overview.txt", "w") as user_file:
            user_file.write(user_overview)

        print("Reports generated successfully.")

    # Read and display reports
    with open("task_overview.txt", "r") as task_file:
        task_overview = task_file.read()
        print(task_overview)

    with open("user_overview.txt", "r") as user_file:
        user_overview = user_file.read()
        print(user_overview)


def display_statistics():
    '''Display statistics'''

    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()

    with open("task_overview.txt", "r") as task_file:
        task_overview = task_file.read()
        print(task_overview)

    with open("user_overview.txt", "r") as user_file:
        user_overview = user_file.read()
        print(user_overview)

# Initialise data
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)

if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

# Main menu loop
while True:
    print()
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    g - Generate Reports
    ds - Display statistics
    e - Exit
    : ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'g':
        generate_reports()
    elif menu == 'ds' and curr_user == 'admin':
        display_statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
