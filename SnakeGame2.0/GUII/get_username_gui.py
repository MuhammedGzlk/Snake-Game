import tkinter as tk

def get_username():
    def submit():
        nonlocal username
        username = entry.get().title()
        root.destroy()

    username = None
    root = tk.Tk()
    root.title("Username")
    root.geometry("300x120")

    label = tk.Label(root, text="Enter your Username:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack()
    entry.focus()

    button = tk.Button(root, text="Start", command=submit)
    button.pack(pady=10)

    root.mainloop()
    return username
