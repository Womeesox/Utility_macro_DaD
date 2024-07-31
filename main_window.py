import tkinter as tk
import macro

def setup_main_window(root):
    root.title("Dark and Darker macro")
    root.geometry("300x200")

    scan_quests_button = tk.Button(root, text="Scan quests", command=macro.scan_quests)
    scan_quests_button.pack(side=tk.TOP, anchor=tk.NE)

    root.mainloop()