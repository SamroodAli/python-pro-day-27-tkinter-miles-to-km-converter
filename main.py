from tkinter import *

# new Tk instance from tkinter
window = Tk()
window.minsize(width=300, height=300)

# Entry widget
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
entry.grid(column=1, row=0)

# Label widget for miles
label = Label(text="Miles")
label.grid(column=2, row=0)

# Label widget for text - is  equal to
label = Label(text="is equal to")
label.grid(column=0, row=1)

# Label widget for result
label = Label(text="0")
label.grid(column=1, row=1)

# Label widget for Km
label = Label(text="Km")
label.grid(column=2, row=1)
# preventing window from closing


# Calculate button event callback
def calculate():
    print("Do something")


# calls calculate() when pressed
button = Button(text="Click Me", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
