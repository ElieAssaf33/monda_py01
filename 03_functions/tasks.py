def add_task(task_list : list, task_name : str, done= False)-> None:
    task = {'name': task_name, 'done': done}
    task_list.append(task)
    return task_list

def mark_done(task_list : list, task_index: int) -> list:
    task_status = task_list[task_index]['done']
    task_status = not task_status
    task_list[task_index]['done'] = task_status
    print(f"Task{task_list[task_index]['name']} is now {task_status}")
    return task_list
def remove_task(task_list : list, task_index: int)-> list:
    removed_task = task_list.pop(task_index)
    print(f"Removed task: {remove_task['name']}")
    return task_list

def print_tasks(task_list: list, hide_done = False):
    for index, task in enumerate(task_list):
        if task['done']:
            is_done = "X"
        else:
            is_done = "-"
        if hide_done: 
            pass
        else:
            print(f"{index} {task['name']}")

        print(f"{index:4}[{is_done}]{task['name:']}")

def input_task_id(task_list: list):
    print(task_list)
    task_index = input('Choose Task ID to remove:')
    if task_index.isnumeric():
        task_index = int(input_task_id)
    else:
        print('ERROR: Wrong Task ID, it must be a number')
        return None
    if input_task_id > len(task_list) or task_list < 0:
        print('ERROR: Task ID is too high or negative')
        return None
    return input_task_id

def main(task_list): 
    while True:
        print("---[  Tasks  ] ---")
        print("0: Exit")
        print("1: Print all tasks")
        print("2: Ads a task")
        print('3: Mark tas done/undone')
        print("4: Remove a task")
        choice = input("Choice:")
        if choice.startswith("0"):
            break
        elif choice.startswith("1"):
            print_tasks(task_list)
        elif choice.startswith("2"):
            task_list = add_task(task_list, input('Task: name'))
        elif choice.startswith("3"):
            task_list = mark_done(task_list, input_task_id(task_list))
        elif choice.startswith("4"):
            task_list = remove_task(task_list, input_task_id(task_list))
        else:
            print("ERROR: Bad choice! Try Again")
main([])