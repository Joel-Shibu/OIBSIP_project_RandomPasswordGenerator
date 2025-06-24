import tkinter as tk
from tkinter import ttk, messagebox, font as tkfont
import pyperclip
from password_utils import generate_password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Configure colors
        self.bg_color = "#f0f2f5"
        self.card_bg = "#ffffff"
        self.primary_color = "#4a6cf7"
        self.text_color = "#333333"
        self.checkbox_bg = "#f8f9fa"
        self.border_color = "#e1e4e8"
        
        # Set window background
        self.root.configure(bg=self.bg_color)
        
        # Main container with padding
        self.main_frame = tk.Frame(root, bg=self.bg_color, padx=30, pady=30)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_font = tkfont.Font(family='Segoe UI', size=20, weight='bold')
        self.title_label = tk.Label(
            self.main_frame,
            text="🔐 Random Password Generator",
            font=title_font,
            bg=self.bg_color,
            fg=self.text_color,
            pady=10
        )
        self.title_label.pack(fill=tk.X)
        
        # Card frame
        self.card = tk.Frame(
            self.main_frame,
            bg=self.card_bg,
            padx=25,
            pady=25,
            highlightthickness=1,
            highlightbackground=self.border_color
        )
        self.card.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Password length control
        self.length_frame = tk.Frame(self.card, bg=self.card_bg)
        self.length_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.length_label = tk.Label(
            self.length_frame,
            text="Password Length:",
            font=('Segoe UI', 10),
            bg=self.card_bg,
            fg=self.text_color
        )
        self.length_label.pack(side=tk.LEFT, anchor='w')
        
        # Password length value display
        self.length_value = tk.StringVar(value="12")
        self.length_display = tk.Entry(
            self.length_frame,
            textvariable=self.length_value,
            font=('Segoe UI', 10),
            width=5,
            justify='center',
            relief='solid',
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.length_display.pack(side=tk.RIGHT, padx=5)
        
        # Character set checkboxes
        self.checkbox_frame = tk.Frame(self.card, bg=self.card_bg)
        self.checkbox_frame.pack(fill=tk.X, pady=10)
        
        # Checkbox style
        self.checkbox_bg = self.card_bg
        self.checkbox_fg = self.text_color
        
        # Uppercase checkbox
        self.uppercase_var = tk.BooleanVar(value=True)
        self.uppercase_cb = tk.Checkbutton(
            self.checkbox_frame,
            text="Include Uppercase",
            variable=self.uppercase_var,
            bg=self.checkbox_bg,
            fg=self.checkbox_fg,
            activebackground=self.checkbox_bg,
            activeforeground=self.checkbox_fg,
            selectcolor=self.checkbox_bg,
            font=('Segoe UI', 10),
            anchor='w'
        )
        self.uppercase_cb.pack(fill=tk.X, pady=2)
        
        # Lowercase checkbox
        self.lowercase_var = tk.BooleanVar(value=True)
        self.lowercase_cb = tk.Checkbutton(
            self.checkbox_frame,
            text="Include Lowercase",
            variable=self.lowercase_var,
            bg=self.checkbox_bg,
            fg=self.checkbox_fg,
            activebackground=self.checkbox_bg,
            activeforeground=self.checkbox_fg,
            selectcolor=self.checkbox_bg,
            font=('Segoe UI', 10),
            anchor='w'
        )
        self.lowercase_cb.pack(fill=tk.X, pady=2)
        
        # Numbers checkbox
        self.numbers_var = tk.BooleanVar(value=True)
        self.numbers_cb = tk.Checkbutton(
            self.checkbox_frame,
            text="Include Numbers",
            variable=self.numbers_var,
            bg=self.checkbox_bg,
            fg=self.checkbox_fg,
            activebackground=self.checkbox_bg,
            activeforeground=self.checkbox_fg,
            selectcolor=self.checkbox_bg,
            font=('Segoe UI', 10),
            anchor='w'
        )
        self.numbers_cb.pack(fill=tk.X, pady=2)
        
        # Symbols checkbox
        self.symbols_var = tk.BooleanVar(value=True)
        self.symbols_cb = tk.Checkbutton(
            self.checkbox_frame,
            text="Include Symbols",
            variable=self.symbols_var,
            bg=self.checkbox_bg,
            fg=self.checkbox_fg,
            activebackground=self.checkbox_bg,
            activeforeground=self.checkbox_fg,
            selectcolor=self.checkbox_bg,
            font=('Segoe UI', 10),
            anchor='w'
        )
        self.symbols_cb.pack(fill=tk.X, pady=2)
        
        # Generate button
        self.generate_btn = tk.Button(
            self.card,
            text="Generate Password",
            command=self.generate_password,
            bg=self.primary_color,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="white",
            font=('Segoe UI', 10, 'bold'),
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.generate_btn.pack(fill=tk.X, pady=(20, 15))
        
        # Password display frame
        self.password_frame = tk.Frame(self.card, bg=self.card_bg)
        self.password_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Password entry
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self.password_frame,
            textvariable=self.password_var,
            font=('Consolas', 12),
            bd=1,
            relief='solid',
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color,
            justify='center',
            readonlybackground='white',
            state='readonly'
        )
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Set initial empty password
        self.password_var.set("")
        
        # Copy button
        self.copy_btn = tk.Button(
            self.password_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard,
            bg="#e9ecef",
            fg=self.text_color,
            activebackground="#dee2e6",
            activeforeground=self.text_color,
            font=('Segoe UI', 9),
            bd=1,
            relief='solid',
            padx=10,
            pady=5,
            cursor="hand2"
        )
        self.copy_btn.pack(side=tk.RIGHT)
        
        # Bind length validation
        self.length_value.trace('w', self.validate_length)
    
    def validate_length(self, *args):
        value = self.length_value.get()
        if value.isdigit():
            num = int(value)
            if num < 1:
                self.length_value.set("1")
            elif num > 64:
                self.length_value.set("64")
        elif value != '':
            self.length_value.set(''.join(filter(str.isdigit, value)) or '8')
    
    def generate_password(self):
        try:
            length = int(self.length_value.get() or 12)
            if length < 1 or length > 64:
                raise ValueError("Password length must be between 1 and 64")
                
            password = generate_password(
                length=length,
                use_uppercase=self.uppercase_var.get(),
                use_lowercase=self.lowercase_var.get(),
                use_digits=self.numbers_var.get(),
                use_symbols=self.symbols_var.get()
            )
            self.password_var.set(password)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
