from auth import signup, login

from stores import Taskstore , Userstore
import getpass


def show_start_options():
    print("\n Welcome to Task manager App")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit\n")

def show_logged_in_options():
    print("\n Logged In Options")
    print("1.Create Task ")
    print("2.View Tasks ")
    print("3.Update Task's Status ")
    print("4. Logout\n")  

def main():

     users = Userstore("task_manager/users.json")
     tasks = Taskstore("task_manager/tasks.json")
     
     show_start_options()
     c = input("Enter your choice ")

     if c == '1':
        signup(users)
     elif c == '2':
        user = login(users)
        if not user:
            return "Login Failed"
        
        user_id = user["user_id"]
        
        print(f"Welcome {user['username']}! You have successfully logged in.")
        
        while True:
            show_logged_in_options()
            ch = input("Enter your choice:")

            if ch == '1':
                tasks.create_task(user_id)

            elif ch == '2':
                tasks.view_tasks(user_id)

            elif ch == '3':
                tasks.mark_task_completed(user_id)

            elif ch == '4':
                print("Logging out!!,Thank you,See you Soon") 
                break 
            
            else:
                print("Invalid option.Please try again")

     elif c == '3':
         print("Exiting the application.Thank you")
         return
     
     else:
         print("Invalid option.Please try again ")
main()                             
