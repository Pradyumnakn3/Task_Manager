from utils import save_json,load_json

import random
from datetime import datetime
 
class Userstore:
    """
    expected user data format:
        {
            "user_id": 9,
            "username": "user7",
            "password": "ajftsesgnkkolkhgyufdydlmjvrw3qsgvjpol3r"
            "created_at": "2026-10-10T10:00:00"
        }
    """

    def __init__(self,path):
        self.path=path
        self.data=load_json(self.path,default={"users":[]})

    def save(self):
        save_json(self.path,self.data)

    def add_user(self,user):
        self.data["users"].append(user)
        self.save()

    def find_user_by_username(self, username):
        for user in self.data["users"]:
            if user["username"] == username:
                return user
            
        return None
    
    def find_user_by_userid(self, user_id):
        for user in self.data['users']:
            if user['user_id'] == user_id:
                return user
            
        return None
    


class Taskstore:
    """
    expected task data format:
        {
            "task_id": "1234",
            "_user_id": 9,
            "task": "Play cricket",
            "status": "pending",
            "created_at": "2026-10-10 10:00:00"
        }
    """

    def __init__(self, path):
        self.path = path
        self.data = load_json(self.path, default={"tasks": []})

    def save(self):
        save_json(self.path, self.data)

    def create_task(self, user_id):
        print("Create a new task")
        text = input("Enter the name of the task: ")

        if not text:
            print("Task cannot be empty")
            return

        task = {
            "task_id": random.randint(1000, 9999),
            "_user_id": user_id,
            "task": text,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.data["tasks"].append(task)
        self.save()
        print("Task created successfully")

    def view_tasks(self, user_id):
        print("\nYour Tasks:")

        user_tasks = []

        for task in self.data["tasks"]:
            if task["_user_id"] == user_id:
                user_tasks.append(task)

        if not user_tasks:
            print("No tasks found")
            return

        for index, task in enumerate(user_tasks, start=1):
            print(index, "-", task["task"], "| Status:", task["status"]) 

    def mark_task_completed(self, user_id):
        user_tasks = []

        for task in self.data["tasks"]:
            if task["_user_id"] == user_id:
                user_tasks.append(task)

        if not user_tasks:
            print("No tasks to update.")
            return

        print("\nYour Tasks:")
        for index, task in enumerate(user_tasks, start=1):
            print(index, "-", task["task"], "| Status:", task["status"])

        choice = (input("Enter task number to mark completed: "))

        if not choice.isdigit():
            print("Invalid input.")
            return
        
        choice = int(choice)
        
        if choice < 1 or choice > len(user_tasks):
            print("Invalid task number.")
            return
        
        user_tasks[choice - 1]["status"] = "completed"
        self.save()

        print("Task marked as completed.")
              