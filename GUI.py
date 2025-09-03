import tkinter as tk

# Function to update the greeting
def greet():
    name = entry.get()
    greeting_label.config(text=f"Hello, {name}!")

# Create the main window
root = tk.Tk()
root.title("Greeter App")
root.geometry("300x150")

# Create an entry widget
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Create a button widget
greet_button = tk.Button(root, text="Greet Me", font=("Arial", 12), command=greet)
greet_button.pack(pady=5)

# Create a label to display the greeting
greeting_label = tk.Label(root, text="", font=("Arial", 14))
greeting_label.pack(pady=10)

# Run the application
root.mainloop()