from tkinter import *

morse_code = {
    "A": "• —",
    "B": "— • • •",
    "C": "— • — •",
    "D": "— • •",
    "E": "•",
    "F": "• • — •",
    "G": "— — •",
    "H": "• • • •",
    "I": "• •",
    "J": "• — — —",
    "K": "— • —",
    "L": "• — • •",
    "M": "— —",
    "N": "— •",
    "O": "— — —",
    "P": "• — — •",
    "Q": "— — • —",
    "R": "• — •",
    "S": "• • •",
    "T": "—",
    "U": "• • —",
    "V": "• • • —",
    "W": "• — —",
    "X": "— • • —",
    "Y": "— • — —",
    "Z": "— — • •",
    "1": "• — — — —",
    "2": "• • — — —",
    "3": "• • • — —",
    "4": "• • • • —",
    "5": "• • • • •",
    "6": "— • • • •",
    "7": "— — • • •",
    "8": "— — — • •",
    "9": "— — — — •",
    "0": "— — — — —",
    " ": "   "
}

def button_clicked():
    text = input.get().upper()
    new_text=""
    for letter in text:
        new_text += morse_code[letter] + " "
    translated_text.config(text=new_text, width=400)

window = Tk()

window.title("Morse Code Converter")
window.geometry("500x300")
window.config(padx=20, pady=20)

input_text = Label(text="Write sentance to convert:", font=("Helvetica", 16, "bold"))
input_text.grid(column=0, row=0, padx=10, pady=10)

input = Entry(width=75)
input.grid(column=0, row=1, padx=5, pady=5)

button = Button(text="Convert", command=button_clicked, padx=5, pady=5, font=("Helvetica", 8, "bold"))
button.grid(column=0, row=2, padx=5, pady=5)

translated_text = Message(width=100, font=("Helvetica", 12, "normal"))
translated_text.grid(column=0, row=3, padx=5, pady=5)

window.mainloop()