# Commit Prompt
## As I have recently started using git for my project, And I often forget to commit my changes so though that a few lines of code could help me with that. 

### What does it do?
Every 10 min it will prompt a window saying **PLEASE COMMIT YOUR CODE**.
And it will do so until we select **QUIT**

### Screeshort 

![](https://github.com/ARjUN-ZORO/Commit-prompt/blob/master/Screenshot%20(65).png)

### Required 
- **Python 3.x** 
- [tkinter](https://github.com/python/cpython/blob/3.8/Doc/library/tk.rst) The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, as well as on Windows systems. (Tk itself is not part of Python; it is maintained at ActiveState.)

### Code 
```python
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

```
### Tip
Insted of running the **.py** everytime you login change it to **.pyw** and paste it in  **C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp**
When you run it as **.py** it will show console log/cmd output and **.pyw** will not.
Want to know [WHY?](https://stackoverflow.com/questions/34739315/pyw-files-in-python-program)
