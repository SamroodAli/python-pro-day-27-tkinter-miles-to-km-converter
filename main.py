from tkinter import *

# new Tk instance from tkinter
window = Tk()
window.config(padx=20, pady=20, bg="green")
# Entry widget
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
entry.grid(column=1, row=0)

# Label widget for miles
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

# Label widget for text - is  equal to
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

# Label widget for result
label_output = Label(text="0")
label_output.grid(column=1, row=1)

# Label widget for Km
label_km = Label(text="Km")
label_km.grid(column=2, row=1)
# preventing window from closing


# Calculate button event callback
def calculate():
    miles = int(entry.get())
    km = str(round(miles*1.60934, 3))
    label_output["text"] = km


# calls calculate() when pressed
button = Button(text="Click Me", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
