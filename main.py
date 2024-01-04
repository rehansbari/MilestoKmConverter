import tkinter


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)


#Label
miles_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=3, row=1)

km_label = tkinter.Label(text="KM", font=("Arial", 24, "bold"))
km_label.grid(column=3, row=2)

text_label = tkinter.Label(text="Is equal to", font=("Arial", 24, "bold"))
text_label.grid(column=1, row=2)

result_label = tkinter.Label(text="", font=("Arial", 24))
result_label.grid(column=2, row=2)

#Button
def button_clicked():
    conversion = int(input.get()) * 1.609
    result_label.config(text=conversion)


button = tkinter.Button(text="Calculate", command=button_clicked)
#button.pack()
button.grid(column=2, row=3)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=2, row=1)



#Always has to be at the end of a program
window.mainloop()