import tkinter as tk
from tkinter import messagebox, ttk

# Task class to represent each task
class Task:
    def __init__(self, title, priority, deadline):
        self.title = title
        self.priority = priority
        self.deadline = deadline

# Main application class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        # Frame for task fields
        self.task_frame = tk.Frame(root)
        
        self.title_label = tk.Label(self.task_frame, text="Task Title")
        self.title_label.pack()

        self.title_entry = tk.Entry(self.task_frame)
        self.title_entry.pack()

        self.priority_label = tk.Label(self.task_frame, text="Priority")
        self.priority_label.pack()

        self.priority_combobox = ttk.Combobox(self.task_frame, values=["Low", "Medium", "High"])
        self.priority_combobox.pack()

        self.deadline_label = tk.Label(self.task_frame, text="Deadline")
        self.deadline_label.pack()

        self.deadline_combobox = ttk.Combobox(self.task_frame, values=["Today", "Tomorrow", "End of Week", "No Deadline"])
        self.deadline_combobox.pack()

        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_frame.pack()

        # Button to show/hide predefined tasks
        self.toggle_tasks_button = tk.Button(root, text="Show Predefined Tasks", command=self.toggle_predefined_tasks)
        self.toggle_tasks_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Predefined tasks (initially hidden)
        self.predefined_tasks = [
            {"title": "Daily Jogging", "priority": "High", "deadline": "Everyday"},
            {"title": "Take Healthy Food", "priority": "Medium", "deadline": "Every Meal"},
            {"title": "Drink Daily 6 Liters of Water", "priority": "High", "deadline": "Everyday"},
        ]

        self.predefined_tasks_visible = False

    # Method to add a new task
    def add_task(self):
        title = self.title_entry.get()
        priority = self.priority_combobox.get()
        deadline = self.deadline_combobox.get()

        if title and priority and deadline:
            task = Task(title, priority, deadline)
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, f"{task.title} (Priority: {task.priority}, Deadline: {task.deadline})")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    # Method to clear input fields after adding a task
    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.priority_combobox.set('')
        self.deadline_combobox.set('')

    # Method to delete a selected task
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    # Method to show/hide predefined tasks
    def toggle_predefined_tasks(self):
        if self.predefined_tasks_visible:
            self.task_listbox.delete(0, tk.END)
            self.predefined_tasks_visible = False
            self.toggle_tasks_button.config(text="Show Predefined Tasks")
        else:
            self.task_listbox.delete(0, tk.END)
            for task_info in self.predefined_tasks:
                task = Task(task_info["title"], task_info["priority"], task_info["deadline"])
                self.tasks.append(task)
                self.task_listbox.insert(tk.END, f"{task.title} (Priority: {task.priority}, Deadline: {task.deadline})")
            self.predefined_tasks_visible = True
            self.toggle_tasks_button.config(text="Hide Predefined Tasks")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
