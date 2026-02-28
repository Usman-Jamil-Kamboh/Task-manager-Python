import tkinter as tk
from tkinter import messagebox
import jsondefs as j

def refresh_tasks():
    listbox.delete(0, tk.END)
    tasks = j.downloadData()
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        listbox.insert(tk.END, f"{task['task_no']} - {task['task']} [{status}]")

def add_task():
    task_name = entry.get().strip()
    if not task_name:
        messagebox.showerror("Error", "Task cannot be empty.")
        return

    tasks = j.downloadData()
    next_id = 1 if not tasks else max(t["task_no"] for t in tasks) + 1

    tasks.append({
        "task_no": next_id,
        "task": task_name,
        "completed": False
    })

    j.uploadData(tasks)
    entry.delete(0, tk.END)
    refresh_tasks()

root = tk.Tk()
root.title("To-Do Manager")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

refresh_tasks()

root.mainloop()