import tkinter as tk
import time


def prompt():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button1 = tk.Button(frame,text='QUIT',fg='red',command=quit)
    button1.pack(side=tk.LEFT)
    button2 = tk.Button(frame,text='Please COMMIT to GIT',command=root.destroy)
    button2.pack(side=tk.LEFT)

    root.mainloop()

while True:
    prompt()
    time.sleep(600)
