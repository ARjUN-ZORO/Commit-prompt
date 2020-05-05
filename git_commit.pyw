import tkinter as tk
import time


def prompt():
    root = tk.Tk()
    root.title("COMMIT TO GIT")
    root.geometry("300x100+200+100")
    frame = tk.Frame(root)
    frame.pack()

    button1 = tk.Button(frame,text='QUIT',fg='red',command=quit)
    button1.pack(side=tk.LEFT)
    # button1.place(x=10,y=80)
    button2 = tk.Button(frame,text='Please COMMIT to GIT',command=root.destroy)
    button2.pack(side=tk.LEFT)
    # button2.place(x=10,y=80)
    # button2.grid(row=1, column=0)


    root.mainloop()

while True:
    prompt()
    time.sleep(600)
