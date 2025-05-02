import tkinter

window1=tkinter.Tk()
window1.title("My First GUI")
window1.geometry("500x500")
window1.configure(bg="black")
label1=tkinter.Label(window1,text="Hello World",font=("Arial",20,"bold"),bg="black",fg="white")
label1.grid(row=0, column=0)
label2=tkinter.Label(window1, text="My name is", font=("Arial", 20, "bold"), bg="black", fg="white")
label2.grid(row=1, column=0)
label3=tkinter.Label(window1, text="Jahad", font=("Arial", 20, "bold"), bg="black", fg="white")
label3.grid(row=2, column=0)



window1.mainloop()

'''
import tkinter

window1=tkinter.Tk()
window1.title("My First GUI")
window1.geometry('800x500')
window1.configure(bg='black')
label1=tkinter.Label(window1,text="Hello World",font=('Arial',20,'bold'),bg='black',fg='white')
label1.pack(pady=20)
def click():
    label1.config(text="Button Clicked")

button1=tkinter.Button(window1, text="Click Me", font=('Arial', 20, 'bold'), bg='white', fg='black', command=click)
button1.pack(pady=20)





window1.mainloop()

'''