import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sunil@12345",
        database="user_registration_db"
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            course VARCHAR(50) NOT NULL,
            duration VARCHAR(10) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user():
    name = name_entry.get()
    age = age_entry.get()
    course = course_var.get()
    duration = duration_var.get()

    if name and age and course and duration:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sunil@12345",
                database="user_registration_db"
            )
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, age, course, duration) 
                VALUES (%s, %s, %s, %s)
            ''', (name, age, course, duration))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "User registered successfully!")
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            course_var.set('')
            duration_var.set('')

            view_users()

        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "An error occurred!")
    else:
        messagebox.showwarning("Input error", "All fields are required!")

def view_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sunil@12345",
        database="user_registration_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    # Clear the listbox before inserting new data
    user_list.delete(0, tk.END)
    
    # Add headers
    headers = f"{'Name':<25}{'Age':<10}{'Course':<20}{'Duration':<15}"
    user_list.insert(tk.END, headers)
    user_list.insert(tk.END, "-" * 80)
    
    # Add each user record
    for user in users:
        formatted_user = f"{user[1]:<25}{user[2]:<10}{user[3]:<20}{user[4]:<15}"
        user_list.insert(tk.END, formatted_user)

root = tk.Tk()
root.title("User Registration")
root.geometry("900x700")  # Adjusted window size for better readability

header = tk.Label(root, text="User Registration Form", font=("Helvetica", 20, "bold"), bg='#004c4c', fg='white')
header.pack(fill='x', pady=15)

form_frame = tk.Frame(root, bg='#87CEEB', padx=20, pady=20, relief="solid", borderwidth=1)
form_frame.pack(pady=20)

# Labels in darker color
label_color = '#003333'

# Name field
tk.Label(form_frame, text="Name", bg='#87CEEB', fg=label_color, font=("Helvetica", 16)).grid(row=0, column=0, sticky="w", padx=20, pady=15)
name_entry = tk.Entry(form_frame, width=40, font=("Helvetica", 14))
name_entry.grid(row=0, column=1, pady=15)

# Age field
tk.Label(form_frame, text="Age", bg='#87CEEB', fg=label_color, font=("Helvetica", 16)).grid(row=1, column=0, sticky="w", padx=20, pady=15)
age_entry = tk.Entry(form_frame, width=40, font=("Helvetica", 14))
age_entry.grid(row=1, column=1, pady=15)

# Course field
tk.Label(form_frame, text="Course", bg='#87CEEB', fg=label_color, font=("Helvetica", 16)).grid(row=2, column=0, sticky="w", padx=20, pady=15)
course_var = tk.StringVar()
course_dropdown = ttk.Combobox(form_frame, textvariable=course_var, values=["MCA", "BCA", "B-TECH", "MBA"], width=37, font=("Helvetica", 14))
course_dropdown.grid(row=2, column=1, pady=15)

# Duration field
tk.Label(form_frame, text="Course Duration", bg='#87CEEB', fg=label_color, font=("Helvetica", 16)).grid(row=3, column=0, sticky="w", padx=20, pady=15)
duration_var = tk.StringVar()
duration_dropdown = ttk.Combobox(form_frame, textvariable=duration_var, values=["2 years", "3 years", "4 years"], width=37, font=("Helvetica", 14))
duration_dropdown.grid(row=3, column=1, pady=15)

# Register Button
register_button = tk.Button(root, text="Register", command=register_user, bg='#00796b', fg='white', font=("Helvetica", 16), width=15)
register_button.pack(pady=20)

# View Users Button
view_button = tk.Button(root, text="View Users", command=view_users, bg='#00796b', fg='white', font=("Helvetica", 16), width=15)
view_button.pack(pady=10)

# Frame for displaying records, matching size and style with the form frame
record_frame = tk.Frame(root, bg="#001f3f", relief="solid", borderwidth=1, padx=15, pady=15)
record_frame.pack(pady=25, padx=25, fill="both", expand=True)

# Title for user list, similar to the header in registration form
list_header = tk.Label(record_frame, text="Registered Users", font=("Helvetica", 16, "bold"), bg="#001f3f", fg="white")
list_header.pack(fill='x')

# Listbox to show user data with scrollbar
user_list = tk.Listbox(record_frame, width=100, height=12, font=("Helvetica", 14), selectbackground='#b2ebf2', justify="left")
user_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(record_frame, orient="vertical")
scrollbar.config(command=user_list.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

user_list.config(yscrollcommand=scrollbar.set)

root.mainloop()
