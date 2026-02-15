import customtkinter as ctk
import math
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculator(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Pro Scientific Calculator")
        self.geometry("420x600")

        self.expression = ""

        self.entry = ctk.CTkEntry(self, font=("Arial", 28), width=380, height=60, justify="right")
        self.entry.pack(pady=20)

        self.create_buttons()

    def create_buttons(self):

        frame = ctk.CTkFrame(self)
        frame.pack()

        buttons = [
            ("7","8","9","/","sin"),
            ("4","5","6","*","cos"),
            ("1","2","3","-","tan"),
            ("0",".","=","+","log"),
            ("C","√","^","π","History")
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = ctk.CTkButton(
                    frame,
                    text=text,
                    width=70,
                    height=50,
                    command=lambda t=text: self.on_click(t)
                )
                btn.grid(row=r, column=c, padx=5, pady=5)

    def on_click(self, char):

        if char == "=":
            try:
                expression = self.expression.replace("^","**")
                expression = expression.replace("√","math.sqrt")
                expression = expression.replace("sin","math.sin")
                expression = expression.replace("cos","math.cos")
                expression = expression.replace("tan","math.tan")
                expression = expression.replace("log","math.log10")
                expression = expression.replace("π",str(math.pi))

                result = str(eval(expression))
                self.save_history(self.expression, result)
                self.entry.delete(0,"end")
                self.entry.insert(0,result)
                self.expression = result
            except:
                self.entry.delete(0,"end")
                self.entry.insert(0,"Error")
                self.expression = ""

        elif char == "C":
            self.expression = ""
            self.entry.delete(0,"end")

        elif char == "History":
            self.show_history()

        else:
            self.expression += str(char)
            self.entry.delete(0,"end")
            self.entry.insert(0,self.expression)

    def save_history(self, exp, result):
        with open("history.txt","a",encoding="utf-8") as f:
            f.write(f"{datetime.now()} | {exp} = {result}\n")

    def show_history(self):
        top = ctk.CTkToplevel(self)
        top.title("History")
        top.geometry("400x300")

        textbox = ctk.CTkTextbox(top)
        textbox.pack(fill="both", expand=True)

        try:
            with open("history.txt","r",encoding="utf-8") as f:
                textbox.insert("end", f.read())
        except:
            textbox.insert("end","No History Yet")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
