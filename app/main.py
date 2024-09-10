# app/main.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app.functions import add_project, add_shift, search_project, list_shifts, search_all_projects
from app.database import init_db

# Initialize the database
init_db()

# Function to create a new project
def create_project():
    name = entry_project_name.get()
    client = entry_client.get()
    if name and client:
        add_project(name, client)
        messagebox.showinfo("Success", "Project added successfully!")
        entry_project_name.delete(0, tk.END)
        entry_client.delete(0, tk.END)
        list_projects()  # Refresh project list after adding
    else:
        messagebox.showwarning("Error", "Please fill out all fields.")

# Function to add a shift
def create_shift():
    project_name = entry_project_name_shift.get()
    hours = entry_hours.get()
    project = search_project(project_name)
    
    if project and hours:
        add_shift(project.id, float(hours))
        messagebox.showinfo("Success", "Shift added successfully!")
        entry_project_name_shift.delete(0, tk.END)
        entry_hours.delete(0, tk.END)
        list_shifts_ui()  # Refresh shift list after adding
    else:
        messagebox.showwarning("Error", "Project not found or invalid hours.")

# Function to list projects in the UI
def list_projects():
    project_list.delete(*project_list.get_children())  # Clear existing list
    projects = search_all_projects()  # Function to get all projects
    for project in projects:
        project_list.insert("", "end", values=(project.id, project.name, project.client))

# Function to list shifts for a project
def list_shifts_ui():
    project_name = entry_project_name_search.get()
    project = search_project(project_name)
    
    if project:
        shifts = list_shifts(project.id)
        result = ""
        for shift in shifts:
            result += f"Date: {shift.date}, Hours Worked: {shift.hours_worked}\n"
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Error", "Project not found.")

# Create the graphical interface with ttk for modern look
root = tk.Tk()
root.title("Billing System - João Carvalho")
root.geometry("600x400")

# Adding a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create the project tab
project_tab = ttk.Frame(notebook)
notebook.add(project_tab, text="Projects")

# Create the shift tab
shift_tab = ttk.Frame(notebook)
notebook.add(shift_tab, text="Shifts")

# Section to add projects (in project_tab)
frame_project = ttk.Frame(project_tab)
frame_project.pack(pady=10)

ttk.Label(frame_project, text="Project Name:").grid(row=0, column=0)
entry_project_name = ttk.Entry(frame_project)
entry_project_name.grid(row=0, column=1)

ttk.Label(frame_project, text="Client Name:").grid(row=1, column=0)
entry_client = ttk.Entry(frame_project)
entry_client.grid(row=1, column=1)

btn_add_project = ttk.Button(frame_project, text="Add Project", command=create_project)
btn_add_project.grid(row=2, column=0, columnspan=2)

# Project list display (in project_tab)
project_list = ttk.Treeview(project_tab, columns=("ID", "Name", "Client"), show='headings', height=8)
project_list.heading("ID", text="ID")
project_list.heading("Name", text="Name")
project_list.heading("Client", text="Client")
project_list.pack(pady=10)

# Section to add shifts (in shift_tab)
frame_shift = ttk.Frame(shift_tab)
frame_shift.pack(pady=10)

ttk.Label(frame_shift, text="Project (for Shift):").grid(row=0, column=0)
entry_project_name_shift = ttk.Entry(frame_shift)
entry_project_name_shift.grid(row=0, column=1)

ttk.Label(frame_shift, text="Hours Worked:").grid(row=1, column=0)
entry_hours = ttk.Entry(frame_shift)
entry_hours.grid(row=1, column=1)

btn_add_shift = ttk.Button(frame_shift, text="Add Shift", command=create_shift)
btn_add_shift.grid(row=2, column=0, columnspan=2)

# Section to search for projects and list shifts (in shift_tab)
frame_search = ttk.Frame(shift_tab)
frame_search.pack(pady=10)

ttk.Label(frame_search, text="Project Name (for Search):").grid(row=0, column=0)
entry_project_name_search = ttk.Entry(frame_search)
entry_project_name_search.grid(row=0, column=1)

btn_list_shifts = ttk.Button(frame_search, text="List Shifts", command=list_shifts_ui)
btn_list_shifts.grid(row=1, column=0, columnspan=2)

# Text field to display found shifts
text_result = tk.Text(shift_tab, height=8, width=50)
text_result.pack(pady=10)

# Initialize the project list
list_projects()

# Start the UI loop
root.mainloop()
