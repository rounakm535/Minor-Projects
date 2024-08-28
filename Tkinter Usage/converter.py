from tkinter import *


def mile_to_km():
    mile = float(mile_inpt.get())
    km = mile * 1.609
    km_val_label.config(text=f"{km}")


window = Tk()
window.title("Distance Converter")
window.config(padx=20, pady=20)

mile_inpt = Entry(width=7)
mile_inpt.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_val_label = Label(text="0")
km_val_label.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
