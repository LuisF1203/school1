import tkinter as tk

app = tk.Tk()
app.geometry("400x200")

entryExample = tk.Entry(app)
entryExample.place(x = 10,
        y = 10,
        width=200,
        height=100)

app.mainloop()
