import datetime
import jsondefs as j
import inputvalidater as i 

date = datetime.datetime.now()
def add():
    tasks = j.downloadData()

    task_name = input("Enter the task name :")
    if not task_name:
        print("Task name cannot be empty ")
        return
    
    if not tasks:
        next_id = 1
    else:
        next_id = max(task["task_no"] for task in tasks) + 1
    
    newtask = {
        "task_no" : next_id,
        "task" : task_name,
        "Date" :  date.strftime("%x"),
        "completed" : False
    }

    tasks.append(newtask)
    j.uploadData(tasks)

    print("added successfully ")


def delete():
    a = j.downloadData()
    
    try:
        d = i.take_int("Enter the task id to delete :")
    except ValueError:
        print("Invalid Input !")
        return

    
    newtasks = []
    found = False
    
    for t in a :
        if t["task_no"] == d:
            found = True
        else:
            newtasks.append(t)
    
    if not found:
        print("task does not found ")
        return
    
    j.uploadData(newtasks)
    
    print("Task deleted successfully ! \n")

def markdone():
    task = j.downloadData()
    if task != [] :
        watch()
        task_id = i.take_int("Enter the tast id to mark it done ")

        found = False
        for x in task:
            if x["task_no"]==task_id :
                found = True
                x['completed'] = True
                break
        if not found:
            print('There is no task with this given id , sorry')
            return 
        j.uploadData(task)
        a = input('Congratulations You have completed your task \n should I delete this task from your todo list ')
        if a.lower() == 'yes':
            delete()
            print('task deleted successfully , congratulations ')
        else:
            print('Ok ! No problem ')
    else:
        print('there are no tasks to mark them done right now ')

def modify():
    tasks = j.downloadData()
    if tasks != []:
        print(tasks)
        id = i.take_int("You can only modify the task name so Enter the task id to modify the name ")

        found = False
        for x in tasks:
            if x["task_no"] == id :
                print(x)
                a = input("Enter the task name to change the privious one ")
                x["task"] = a
                print('task name is changed successfully \n\n')
                found = True
        if not found:
            print('There is no task with this given id ')
            
        j.uploadData(tasks)
    else:
        print('Task list is empty right now ')

def watch():
    tasks = j.downloadData()
    if tasks != []:
        print("\nYour Tasks:\n")

        for task in tasks:
            status = "✔ Done" if task["completed"] else "✘ Pending"
            print(f"""
                ID      : {task['task_no']}
                Task    : {task['task']}
                Date    : {task['Date']}
                Status  : {status}
                ---------------------------
                """)
    else:
        print('task list is empty right now ')

