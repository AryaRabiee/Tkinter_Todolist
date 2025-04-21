import tkinter as tk
from tkinter import messagebox ,filedialog

class Todo:
    def __init__(self , window):
        self.window = window
        self.window.geometry('460x520')
        self.window.title("Todo_List")
        self.window.config(bg = '#98FB98')
        self.counter = 1
        self.todo_list = []

        self.entery = tk.Entry(self.window ,font=("" , 18),width=15)
        self.entery.place(x=20 , y = 250)
        self.label = tk.Label(self.window , text="Enter your Task :" , width=13,height=1, font=("Arial", 14),bg='#98FB98')
        self.label.place(x=20,y=210)
        self.add_btn = tk.Button(self.window,text="Add task" , width=27,height=1 , bg='white', command=self.add_task)
        self.add_btn.place(x=20 , y=290)
        self.delete_btn = tk.Button(self.window , text="Delete Task" , width=27,height=1 , bg='red' , command=self.delete_task)
        self.delete_btn.place(x=20 , y=330)
        self.clear_btn = tk.Button(self.window,text="Clear All Tasks" ,width=27,height=1 , bg='white',command=self.clear_task )
        self.clear_btn.place(x=20 , y=370)
        self.exit_btn = tk.Button(self.window,text="Exit" ,width=27,height=1,bg='white', command=self.exit)
        self.exit_btn.place(x=20 , y=410)
        self.save = tk.Button(self.window,text="Save" ,width=27,height=1,bg='green', command=self.save_task)
        self.save.place(x=20 , y=450)
        self.area = tk.Listbox(self.window , height=18,width=33)
        self.area.place(x=245 , y=140)



    def add_task(self):
        user_input = self.entery.get()
        if user_input.strip():
            text = f'{self.counter} ) {user_input}'
            self.area.insert(tk.END , text)
            self.counter +=1
            self.entery.delete(0,tk.END)
            self.todo_list.append(text)
        else:
            messagebox.showinfo("Add Task" , 'Please enter a task.')

    def delete_task(self):
        try:
            selected_task = self.area.curselection()[0]
            self.area.delete(selected_task)
        except:
            messagebox.showerror("Error" , "No task selected")

    def clear_task(self):

        self.area.delete(0,tk.END)
        self.counter = 1



    def exit(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if answer:
            self.window.quit()


    

    def save_task(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    for task in self.area.get(0, tk.END):
                        file.write(task + '\n')
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

        


window = tk.Tk()
todi_app =Todo(window)
window.mainloop()