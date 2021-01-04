"""A simple tkinter miles to kilometer module"""
from tkinter import *


FONT = ("Ariel", 20, "italic")

# new Tk instance from tkinter
window = Tk()
window.config(padx=20, pady=20, bg="red")

# Entry widget
entry = Entry(width=10, font=FONT)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
entry.grid(column=1, row=0)

# Label widget for miles
label_miles = Label(text="Miles", padx=10, pady=10, bg="red", font=FONT, fg="white")
label_miles.grid(column=2, row=0)

# Label widget for text - is  equal to
label_equal = Label(text="is equal to",  padx=10, pady=10, bg="red", font=FONT, fg="white")
label_equal.grid(column=0, row=1)

# Label widget for result
label_output = Label(text="0",  padx=10, pady=10, bg="red", font=FONT, fg="white")
label_output.grid(column=1, row=1)

# Label widget for Km
label_km = Label(text="Km",  padx=10, pady=10, bg="red", font=FONT, fg="white")
label_km.grid(column=2, row=1)
# preventing window from closing


# Calculate button event callback
def calculate():
    """Button event listener callback to convert miles to Km"""
    miles = int(entry.get())
    kilo_meters = str(round(miles*1.60934, 3))
    label_output["text"] = kilo_meters


# calls calculate() when pressed
button = Button(text="Click Me", command=calculate, font=FONT,
                width=9, bg="navy", fg="white", highlightcolor="navy")
button.grid(column=1, row=2)

# Preventing window from closing
window.mainloop()

