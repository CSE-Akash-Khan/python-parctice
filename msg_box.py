#tutorial = 237
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()

#* label frame
label_frame = ttk.LabelFrame(win, text = 'Contact details')
label_frame.grid(row = 0,column = 0,padx = 40,pady = 10)

#* labels
name_label = ttk.Label(label_frame,text = 'Enter your name: ',font = ('Helvetica','12'))
age_label = ttk.Label(label_frame,text = 'Enter your age: ',font = ('Helvetica','12'))

#* Entry box variable
name_var = tk.StringVar()
age_var = tk.StringVar()

#*Entry box
name_entry = ttk.Entry(label_frame,width = 36,textvariable = name_var)
age_entry = ttk.Entry(label_frame,width = 36,textvariable = age_var)

#* grid
name_label.grid(row = 0,column = 0,padx = 5,pady = 5,sticky = tk.W)
age_label.grid(row = 0,column = 1,padx = 5,pady = 5,sticky = tk.W)
name_entry.grid(row = 1,column = 0,padx = 5,pady = 5,sticky = tk.W)
age_entry.grid(row = 1,column = 1,padx = 5,pady = 5,sticky = tk.W)

#* submit button
def submit():
    # m_box.showinfo('title','content of this message box')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '': #name and age er jodi konota miss kore ta hole error show korbe
        m_box.showerror('Error','Please fill bouth name and age')
    else:
        try:
            #age = 'hjkhlkasd' or age = '20' #? user ja input korbe ta string ee hobe tobe amader data base ee store korte hobe number kono char store kora jabena        
            age = int(age)#age = '20' jodi  user eirokom kono int type sonkha pass kore ta hole try block cholebe r ta na hole wxcept bolock cholbe
        except ValueError:
            m_box.showerror('error','only degit are allowed in age field')
        else:
            if age < 18:
                m_box.showwarning('error',"it's only allowed for avobe 18+ person")
            else:
                print(f"{name} : {age}")
                # m_box.showinfo('your name and age',f"{name} : {age}")

submit_btn = ttk.Button(win,text = 'Submit',command = submit)
submit_btn.grid(row = 1,columnspan = 2,padx = 40)
win.mainloop()


