Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import sklearn
>>> from sklearn.feature_extraction.text import CountVectorizer
>>> from sklearn.naive_bayes import MultinomialNB
>>> from sklearn.pipeline import make_pipeline
>>> import random
>>> # Initialize an empty task list
... tasks = pd.DataFrame (columns = ['description','priority'])
>>> # Load pre-existing tasks from a CSV file
... try:
...   tasks = pd.read_csv('tasks.csv')
... except FileNotFoundError:
...   pass
... 
>>> # Function to save tasks to a CSV file
... def save_tasks():
...   tasks.to_csv('tasks.csv', index = False)
... 
...   
>>> # Train the task priority classifier
vectorizer = CountVectorizer()
clf = MultinomialNB()
model = make_pipeline(vectorizer, clf)
print(tasks.head())
Empty DataFrame
Columns: [description, priority]
Index: []
tasks = pd.read_csv("C:\\Users\\LOHIDAS\\Downloads\\basic (1)\\basic\\tasks.csv")
tasks.head()
                            description priority
0                         buy groceries     high
1               complete project report   medium
2      schedule a meeting with the team      low
3  prepare presentation for the meeting   medium
4                         pay the bills     high
tasks.columns
Index(['description', 'priority'], dtype='object')
model.fit(tasks['description'], tasks['priority'])
Pipeline(steps=[('countvectorizer', CountVectorizer()),
                ('multinomialnb', MultinomialNB())])
# Function to add a task to the list
def add_task(description, priority):
    global tasks  # Declare tasks as a global variable
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks()

    
# Function to remove a task by description
def remove_task(description):
    tasks = tasks[tasks['description'] != description]
    save_tasks()

    
# Function to list all tasks
def list_tasks():
    if tasks.empty:
        print("No tasks available.")
    else:
        print(tasks)

        
# Function to recommend a task based on machine learning
def recommend_task():
    if not tasks.empty:
        # Get high-priority tasks
        high_priority_tasks = tasks[tasks['priority'] == 'high']

        if not high_priority_tasks.empty:
            # Choose a random high-priority task
            random_task = random.choice(high_priority_tasks['description'])
            print(f"Recommended task: {random_task} - Priority: high")
        else:
            print("No high-priority tasks available for recommendation.")
    else:
        print("No tasks available for recommendations.")

        
# Main menu
while True:
    print("\nTask Management App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Recommend Task")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        priority = input("Enter task priority (low/medium/high): ").capitalize()
        add_task(description, priority)
        print("Task added successfully.")

    elif choice == "2":
        description = input("Enter task description to remove: ")
        remove_task(description)
        print("Task removed successfully.")

    elif choice == "3":
        list_tasks()

    elif choice == "4":
        recommend_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")


Task Management App
1. Add Task
2. Remove Task
3. List Tasks
4. Recommend Task
5. Exit
Select an option: 1
Enter task description: exercise
Enter task priority (low/medium/high): medium
Task added successfully.

Task Management App
1. Add Task
2. Remove Task
3. List Tasks
4. Recommend Task
5. Exit
Select an option: 3
                            description priority
0                         buy groceries     high
1               complete project report   medium
2      schedule a meeting with the team      low
3  prepare presentation for the meeting   medium
4                         pay the bills     high
5                              exercise      low
6                              exercise   Medium

Task Management App
1. Add Task
2. Remove Task
3. List Tasks
4. Recommend Task
5. Exit
Select an option: 5
Goodbye!
