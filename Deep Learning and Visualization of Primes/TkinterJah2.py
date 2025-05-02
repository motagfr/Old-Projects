import tkinter

def show_hello():
    print("Hello")

def add(num1,num2):
    print(num1+num2)

window1 = tkinter.Tk()
window1.geometry("500x250")
window1.title("My First GUI Program")

# Create
lbl1 = tkinter.Label(window1, text="Enter Your Age:",width=20)
# Locate
lbl1.grid(row=0, column=0)

textbox1 = tkinter.Entry(window1, width=25, bg="#000000", fg="#FFFFFF")
textbox1.grid(row=0, column=1)

btn1 = tkinter.Button(window1, text="Click Me!", width=45,border=1,pady=10,command=show_hello)
btn1.grid(row=1, column=0, columnspan=2,padx=10,pady=10)

btn2=tkinter.Button(window1,text="Second Button",command=lambda:add(2,6))
btn2.grid(row=2,column=0)

window1.mainloop()
