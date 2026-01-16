        # Enable it
import tkinter as tk

def toggle_button_state():
    # Check the button's current state
    if my_button['state'] == 'normal':
        # Disable it
        my_button.config(state="disabled", text="I am disabled!")
    else:
        # Enable it
        my_button.config(state="normal", text="I am enabled!")

root = tk.Tk()
root.title("Toggle Button Example")
root.geometry("300x150")

# Button to toggle the other button
toggler = tk.Button(root, text="Toggle Button", command=toggle_button_state)
toggler.pack(pady=10)

# The button to be toggled
my_button = tk.Button(root, text="I am enabled!")
my_button.pack(pady=10)
my_button = tk.Button(root, text="I am disabled!")
my_button.pack(pady=10)

root.mainloop()
