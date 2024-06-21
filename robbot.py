import tkinter as tk
import subprocess
import sys

class RobbotApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-topmost', True)  # Keep the window on top

        self.frame = tk.Frame(self.root, bg='lightgray')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.text_field = tk.Entry(self.frame, font=('Arial', 11))
        self.text_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.close_button = tk.Button(self.frame, text='x', command=self.close_app, bg='cyan4', fg='white')
        self.close_button.pack(side=tk.RIGHT)

        self.text_field.bind('<Return>', self.start_jupyter_lab)
        self.frame.bind('<Button-1>', self.start_move)
        self.frame.bind('<B1-Motion>', self.do_move)

        self.position_window()

    def position_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 200
        window_height = 30
        x_position = screen_width - window_width - 10
        y_position = screen_height - window_height - 50
        self.root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')
        print(f'Window positioned at {x_position}, {y_position} on a screen of {screen_width}x{screen_height}')

    def start_jupyter_lab(self, event):
        import bia_bob

        text = self.text_field.get()

        if len(text) == 0:
            return

        filename = bia_bob._notebook_generation.generate_notebook(f"""
Generate a Python Jupyter notebook that contains "import bia_bob" as a code cell and answers this request: 
{text}
""")
        self.set_text_field("")
        
        subprocess.Popen([sys.executable, '-m', 'jupyter', 'lab', filename])

    def set_text_field(self, text):
        self.text_field.delete(0, tk.END)  # Clear current text
        self.text_field.insert(0, text)    # Insert new text

    def close_app(self):
        self.root.destroy()

    def start_move(self, event):
        self.root.x = event.x
        self.root.y = event.y

    def do_move(self, event):
        x = self.root.winfo_pointerx() - self.root.x
        y = self.root.winfo_pointery() - self.root.y
        self.root.geometry(f'+{x}+{y}')

if __name__ == '__main__':
    root = tk.Tk()
    app = RobbotApp(root)
    root.mainloop()
