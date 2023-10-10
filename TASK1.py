{\rtf1\ansi\ansicpg1252\cocoartf2757
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # TASK_1\
\
class ToDoList:\
    def __init__(self):\
        self.tasks = []\
\
    def add_task(self, task):\
        self.tasks.append(task)\
        print(f"Task '\{task\}' added to the to-do list.")\
\
    def remove_task(self, task):\
        if task in self.tasks:\
            self.tasks.remove(task)\
            print(f"Task '\{task\}' removed from the to-do list.")\
        else:\
            print(f"Task '\{task\}' not found in the to-do list.")\
\
    def list_tasks(self):\
        if self.tasks:\
            print("To-Do List:")\
            for index, task in enumerate(self.tasks, start=1):\
                print(f"\{index\}. \{task\}")\
        else:\
            print("To-Do List is empty.")\
\
def main():\
    to_do_list = ToDoList()\
\
    while True:\
        print("\\nOptions:")\
        print("1. Add Task")\
        print("2. Remove Task")\
        print("3. List Tasks")\
        print("4. Exit")\
\
        choice = input("Enter your choice: ")\
\
        if choice == "1":\
            task = input("Enter the task: ")\
            to_do_list.add_task(task)\
        elif choice == "2":\
            task = input("Enter the task to remove: ")\
            to_do_list.remove_task(task)\
        elif choice == "3":\
            to_do_list.list_tasks()\
        elif choice == "4":\
            print("Exiting the To-Do List application.")\
            break\
        else:\
            print("Invalid choice. Please select a valid option.")\
\
if __name__ == "__main__":\
    main()\
}