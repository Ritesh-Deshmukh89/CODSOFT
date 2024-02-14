import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = self.load_tasks()
        
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(padx=20, pady=10)
        
        self.task_list = tk.Listbox(self.task_list_frame, width=50, height=15)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)
        
        self.update_task_list()
    
    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "[X]" if task["completed"] else "[ ]"
            self.task_list.insert(tk.END, f"{status} {task['title']}")
    
    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            new_task = {"title": title, "completed": False}
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_task_list()
    
    def edit_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            title = simpledialog.askstring("Edit Task", "Enter new task title:", initialvalue=self.tasks[selected_task_index[0]]["title"])
            if title:
                self.tasks[selected_task_index[0]]["title"] = title
                self.save_tasks()
                self.update_task_list()
    
    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            confirmed = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirmed:
                del self.tasks[selected_task_index[0]]
                self.save_tasks()
                self.update_task_list()
    
    def complete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.save_tasks()
            self.update_task_list()
    
    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
