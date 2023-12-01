import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500") 
        self.root.resizable(False, False)  
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font=('Arial', 24), justify='right', bd=10, insertwidth=4, width=14)
        self.entry.grid(row=0, column=0, columnspan=4, ipady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, font=('Arial', 18), command=lambda button=button: self.on_click(button) if button != '=' else self.calculate(), width=4, height=2).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text='C', font=('Arial', 18), command=self.clear_entry, width=4, height=2).grid(row=row_val, column=col_val, sticky='nsew')

        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i - 1, weight=1)

    def on_click(self, button_value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current + str(button_value))

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
