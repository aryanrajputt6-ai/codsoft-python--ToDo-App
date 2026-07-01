import tkinter as tk

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, "• " + task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def mark_done():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(selected, "✔ " + task)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.config(bg="#1e1e2f")

# ---------------- TITLE ---------------- #

title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=15)

# ---------------- ENTRY ---------------- #

entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=10)

# ---------------- BUTTON FRAME ---------------- #

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

add_button = tk.Button(frame, text="Add", bg="#4CAF50", fg="white",
                       width=10, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(frame, text="Delete", bg="#f44336", fg="white",
                          width=10, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(frame, text="Save", bg="#2196F3", fg="white",
                        width=10, command=save_tasks)
save_button.grid(row=0, column=2, padx=5)

done_button = tk.Button(frame, text="Done ✔", bg="#FFC107",
                        width=22, command=mark_done)
done_button.grid(row=1, column=0, columnspan=3, pady=8)

# ---------------- LISTBOX + SCROLLBAR ---------------- #

frame_list = tk.Frame(root)
frame_list.pack(pady=10)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, width=35, height=12,
                     font=("Arial", 12),
                     yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# ---------------- LOAD TASKS ---------------- #

load_tasks()

# ---------------- RUN APP ---------------- #

root.mainloop()