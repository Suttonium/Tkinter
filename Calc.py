from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title("Calculator")
main_window.resizable(0, 0)  # this window's size cannot be changed


class Application(Frame):
    display = None

    def __init__(self, master_window, *args, **kwargs):
        Frame.__init__(self, master_window, *args, **kwargs)
        self.display = Entry(self, font=('Helvetica', 16), relief=RAISED, justify=RIGHT, borderwidth=0)
        self.create_widgets()

    def append_to_display(self, text):
        entry_text = self.display.get(,,
                     text_length = len(entry_text)

        if entry_text == "0":
            self.replace_text(text)
        else:
            self.display.insert(text_length, text)

    def replace_text(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def clear_text(self):
        self.display.delete(0, END)
        self.display.insert(0, "0")

    def calculate_expression(self):
        expression = self.display.get(,,
                     expression = expression.replace("%", "/100")

        try:
            result = eval(expression)
            self.replace_text(result)
        except:
            messagebox.showinfo("Error", "Invalid Input")

    def create_widgets(self):
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        seven_button = Button(self, font=('Helvetica', 11), text="7", borderwidth=0, command=lambda: self.append_to_display("7"))
        seven_button.grid(row=1, column=0, sticky="NWNESWSE")  # sticky makes the button expand in each direction to fit

        eight_button = Button(self, font=('Helvetica', 11), text="8", borderwidth=0, command=lambda: self.append_to_display("8"))
        eight_button.grid(row=1, column=1, sticky="NWNESWSE")

        nine_button = Button(self, font=('Helvetica', 11), text="9", borderwidth=0, command=lambda: self.append_to_display("9"))
        nine_button.grid(row=1, column=2, sticky="NWNESWSE")

        multiplication_button = Button(self, font=('Helvetica', 11), text="*", borderwidth=0, command=lambda: self.append_to_display("*"))
        multiplication_button.grid(row=1, column=3, sticky="NWNESWSE")

        clear_button = Button(self, font=('Helvetica', 11), text="C", borderwidth=0, command=self.clear_text)
        clear_button.grid(row=1, column=4, sticky="NWNESWSE")

        four_button = Button(self, font=('Helvetica', 11), text="4", borderwidth=0, command=lambda: self.append_to_display("4"))
        four_button.grid(row=2, column=0, sticky="NWNESWSE")

        five_button = Button(self, font=('Helvetica', 11), text="5", borderwidth=0, command=lambda: self.append_to_display("5"))
        five_button.grid(row=2, column=1, sticky="NWNESWSE")

        six_button = Button(self, font=('Helvetica', 11), text="6", borderwidth=0, command=lambda: self.append_to_display("6"))
        six_button.grid(row=2, column=2, sticky="NWNESWSE")

        division_button = Button(self, font=('Helvetica', 11), text="/", borderwidth=0, command=lambda: self.append_to_display("/"))
        division_button.grid(row=2, column=3, sticky="NWNESWSE")

        percentage_button = Button(self, font=('Helvetica', 11), text="%", borderwidth=0, command=lambda: self.append_to_display("%"))
        percentage_button.grid(row=2, column=4, sticky="NWNESWSE")

        one_button = Button(self, font=('Helvetica', 11), text="1", borderwidth=0, command=lambda: self.append_to_display("1"))
        one_button.grid(row=3, column=0, sticky="NWNESWSE")

        two_button = Button(self, font=('Helvetica', 11), text="2", borderwidth=0, command=lambda: self.append_to_display("2"))
        two_button.grid(row=3, column=1, sticky="NWNESWSE")

        three_button = Button(self, font=('Helvetica', 11), text="3", borderwidth=0, command=lambda: self.append_to_display("3"))
        three_button.grid(row=3, column=2, sticky="NWNESWSE")

        subtraction_button = Button(self, font=('Helvetica', 11), text="-", borderwidth=0, command=lambda: self.append_to_display("-"))
        subtraction_button.grid(row=3, column=3, sticky="NWNESWSE")

        equality_button = Button(self, font=('Helvetica', 11), text="=", borderwidth=0, command=self.calculate_expression)
        equality_button.grid(row=3, column=4, sticky="NWNESWSE", rowspan=2)

        zero_button = Button(self, font=('Helvetica', 11), text="0", borderwidth=0, command=lambda: self.append_to_display("0"))
        zero_button.grid(row=4, column=0, sticky="NWNESWSE", columnspan=2)

        dot_button = Button(self, font=('Helvetica', 11), text=".", borderwidth=0, command=lambda: self.append_to_display("."))
        dot_button.grid(row=4, column=2, sticky="NWNESWSE")

        addition_button = Button(self, font=('Helvetica', 11), text="+", borderwidth=0, command=lambda: self.append_to_display("+"))
        addition_button.grid(row=4, column=3, sticky="NWNESWSE")


runnable = Application(main_window).grid()
main_window.mainloop()
