import tkinter as tk
from tkinter import messagebox
import webbrowser

class TuringMachineSim(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turing Machine Simulator")
        self.geometry("800x600")
        self.create_welcome_page()
    
    def create_welcome_page(self):
        self.configure(bg="#1E90FF")

        tk.Label(self, text="Turing Machine Simulator", bg="#1E90FF",
                 fg="white", 
                    font=('Helvetica', 32, "bold")).pack(pady=50)
        
        tk.Button(self, text="Start Simulation", bg="white", fg="#1E90FF",
                  font=('sans-serif', 16), command=self.create_options_page).pack(pady=20)
        
        self.credits()
    
    def create_options_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.configure(bg="#ADD8E6")

        tk.Label(self, text="Select Simulation Options", bg="#ADD8E6", font=('Verdana', 16)).pack(pady=20)

        options = [
            ("String should accept odd one's and even zero's", 0),
            ("String should accept even one's and odd zero's", 1),
            ("String should accept even one's and even zero's", 2),
            ("String should accept odd one's and odd zero's", 3)
        ]
        self.selected_option = tk.IntVar()

        for option, value in options:
            tk.Radiobutton(self, text=option, variable=self.selected_option,
                           value=value, bg="#ADD8E6", font=('Verdana', 12)).pack(pady=10)
        
        tk.Button(self, text="Proceed", bg="white", fg="#1E90FF",
                  font=('sans-serif', 16), command=self.create_input_page).pack(pady=30)
        
        self.credits()

    def create_input_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.configure(bg="#90EE90")
        tk.Label(self, text="Enter Input String", bg="#90EE90", font=('Verdana', 16)).pack(pady=20)
        self.string_input = tk.Entry(self, font=('Calibri', 14))
        self.string_input.pack(pady=10)

        tk.Button(self, text="Check", bg="#FFFACD", 
        font=('sans-serif', 16), command=self.check_string).pack(pady=30)
            
        self.credits()
        
    def check_string(self):
        string = self.string_input.get()
        option = self.selected_option.get()
        if option == 0:
            if self.accept_odd_ones_even_zeros(string):
                messagebox.showinfo("Result", f"The String '{string}' Accepted")
            else:
                messagebox.showinfo("Result", f"The String '{string}' Rejected")
        elif option == 1:
            if self.accept_even_ones_odd_zeros(string):
                    messagebox.showinfo("Result", f"The String '{string}' Accepted")
            else:
                    messagebox.showinfo("Result", f"The String '{string}' Rejected")
        elif option == 2:
            if self.accept_even_ones_even_zeros(string):
                    messagebox.showinfo("Result", f"The String '{string}' Accepted")
            else:
                    messagebox.showinfo("Result", f"The String '{string}' Rejected")
        elif option == 3:
            if self.accept_odd_ones_odd_zeros(string):
                    messagebox.showinfo("Result", f"The String '{string}' Accepted")
            else:
                    messagebox.showinfo("Result", f"The String '{string}' Rejected")

        restart_button = tk.Button(self, text="Restart", bg="white", fg="#1E90FF",
                                       font=('sans-serif', 16), command=self.restart)
        restart_button.pack(side="left" ,padx=115 ,pady=30)

        exit_button = tk.Button(self, text="Exit", bg="white", fg="#1E90FF",
                                    font=('sans-serif', 16), command=self.exit)
        exit_button.pack(side="left", padx=125, pady=30)
    
    def accept_odd_ones_even_zeros(self, string):
        state = 0
        for symbol in string:
            if state == 0:
                if symbol == '0':
                   state = 2
                elif symbol == '1':
                    state = 1
                else:
                    return False
            elif state == 1:
                if symbol == '0':
                    state = 3
                elif symbol == '1':
                    state = 0
                else:
                    return False
            elif state == 2:
                if symbol == '0':
                    state = 0
                elif symbol == '1':
                    state = 3
                else:
                    return False
            elif state == 3:
                if symbol == '0':
                    state = 1
                elif symbol == '1':
                    state = 2
                else:
                    return False
        return state == 3
    
    def accept_even_ones_odd_zeros(self, string):
        state = 0
        for symbol in string:
            if state == 0:
                if symbol == '0':
                   state = 1
                elif symbol == '1':
                    state = 2
                else:
                    return False
            elif state == 1:
                if symbol == '0':
                    state = 0
                elif symbol == '1':
                    state = 3
                else:
                    return False
            elif state == 2:
                if symbol == '0':
                    state = 3
                elif symbol == '1':
                    state = 2
                else:
                    return False
            elif state == 3:
                if symbol == '0':
                    state = 2
                elif symbol == '1':
                    state = 1
                else:
                    return False
        return state == 1
    
    def accept_even_ones_even_zeros(self, string):
        state = 0
        for symbol in string:
            if state == 0:
                if symbol == '0':
                   state = 1
                elif symbol == '1':
                    state = 2
                else:
                    return False
            elif state == 1:
                if symbol == '0':
                    state = 2
                elif symbol == '1':
                    state = 1
                else:
                    return False
            elif state == 2:
                if symbol == '0':
                    state = 1
                elif symbol == '1':
                    state = 2
                else:
                    return False
            elif state == 3:
                if symbol == '0':
                    state = 2
                elif symbol == '1':
                    state = 1
                else:
                    return False
        return state == 2
    
    def accept_odd_ones_odd_zeros(self, string):
        state = 0
        for symbol in string:
            if state == 0:
                if symbol == '0':
                   state = 1
                elif symbol == '1':
                    state = 2
                else:
                    return False
            elif state == 1:
                if symbol == '0':
                    state = 0
                elif symbol == '1':
                    state = 3
                else:
                    return False
            elif state == 2:
                if symbol == '0':
                    state = 3
                elif symbol == '1':
                    state = 0
                else:
                    return False
            elif state == 3:
                if symbol == '0':
                    state = 2
                elif symbol == '1':
                    state = 1
                else:
                    return False
        return state == 3
    
    

    def restart(self):
        for widget in self.winfo_children():
             widget.destroy()
        self.create_welcome_page()

    def exit(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.exit_frame = tk.Frame(self, bg="#FF6347")
        self.exit_frame.pack(fill="both", expand=True)

        self.exit_label = tk.Label(self.exit_frame, font=('Helvetica', 24))

        self.exit_label.config(text="Thank You for Using the Turing Machine Simulator!\n")
        self.exit_label.pack()
        self.after(1000, self.destroy)

    def credits(self):
        credit_frame = tk.Frame(self, bg=self['bg'])
        credit_frame.pack(side="bottom", pady=10)

        credit_label = tk.Label(credit_frame, text="Developed by Belal Ashraf, Omar Hossam, and Mohamed Ezzat", bg=self['bg'], font=('Arial', 10))
        credit_label.pack(side="left")

        link = tk.Label(credit_frame, text="GitHub", fg="blue", cursor="hand2", bg=self['bg'], font=('Arial', 10, "underline"))
        link.pack(side="left", padx=10)
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Beloman-bolobol999"))


if __name__ == "__main__":
    app = TuringMachineSim()
    app.mainloop()