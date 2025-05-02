import tkinter

window1 = tkinter.Tk()
window1.title("My First GUI")
window1.geometry("800x800")  # Here numbers are in pixel terms
window1.configure(bg="grey")
label1 = tkinter.Label(
    window1, text="Enter your age: ", font=("Arial", 20, "bold"), bg="black", fg="white"
)
label1.grid(row=0, column=0)
textbox1 = tkinter.Entry(
    window1, font=("Arial", 20, "bold"), width=10
)  # width is how many characters are visible at a time
textbox1.grid(row=0, column=1)
btn1=tkinter.Button(window1, text="Click Me", font=('Arial', 20, 'bold'), bg='white', 
                    fg='black').grid(row=1, column=0)


window1.mainloop()
window1.mainloop()
window1.mainloop()
window1.mainloop()
window1.mainloop()




