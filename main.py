tasks = [
    {'name' : 'Write email to Jan', 'completed' : True},
    {'name' : 'Sweep front porch', 'completed' : True},
    {'name' : 'Call mom', 'completed' : False}
]
def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))
def add_task():
    task_text = input('Please add a task: ')
    new_task= {'name': task_text, 'completed': False}
    tasks.append(new_task)
def remove_task():
    list_tasks()
    remove_task = int(input('Please enter the number of the task you want removed: '))
    tasks.remove(tasks[remove_task])
def completed_task(): 
    list_tasks()
    completed_task= int(input('Please enter the number of the task that you completed: '))
    tasks[completed_task]['completed'] = True
menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = input(menu_text)
    if decision == '1':
        list_tasks()
    elif decision == "2":
        add_task()
    elif decision == "3":
        remove_task()
    elif decision == "4":
        completed_task()
    elif decision == '5':
        program_is_running = False
    else:
        print('please choose a valid option')


