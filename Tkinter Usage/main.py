from tkinter import  *

window = Tk()
window.title("Developed by Rounak")
window.minsize(width= 600, height= 600)
window.config(padx= 20, pady= 20)


my_label = Label(text= "Me label", font=("Arial", 24, "bold"))
my_label.grid(column= 0, row= 0)



my_label["text"] = "New text"
my_label.config(text = "New Text")


def click():
    print("I got Clicked..")
    new_txt = inpt.get()
    my_label.config(text= new_txt)

new_butt = Button(text="Hii...", command= click)
new_butt.grid(column= 2, row= 0)

button = Button(text="Click Here", command= click)
button.grid(column= 1, row= 1)

inpt = Entry(width = 10)
inpt.grid(column= 4, row= 2)
ion = inpt.get()
print(ion)


window.mainloop()