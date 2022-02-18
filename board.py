import tkinter as tk

window = tk.Tk()

for i in range(9):
    for j in range(9):
        button = tk.Button(
            master=window,
            text = "Row" + str(i) +"\nColumn" + str(j),
            bg='black', fg='white'
        )
        button.grid(row=i, column=j,padx=0, pady=0, ipadx=0, ipady=0)
button = tk.Button(master=window,text = "Row 8\nColumn 8")
button.grid(row=9, column=9,padx=0, pady=0, ipadx=0, ipady=0,columnspan=5, rowspan=5)

window.mainloop()
