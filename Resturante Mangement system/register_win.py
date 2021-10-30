from tkinter import* 
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import random

class Register_win:
     def __init__(self, root):
          self.root = root
          self.root.title("Register")
          self.root.geometry("1550x800+0+0")



          # Variables for storing Values
          self.var_f_name = StringVar()
          self.var_l_name = StringVar()
          self.var_contact_num = StringVar()
          self.var_email_id = StringVar()
          self.var_security_question = StringVar()
          self.var_security_answer = StringVar()
          self.var_passwd = StringVar()
          self.var_confirm_passwd = StringVar()



          # All Images 
          all_img = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
          random_img = random.choice(all_img)

          self.bg = ImageTk.PhotoImage(file = rf"G:\Peoples Projects\Anuraag TY Peoject\Resturante Mangement system\bg-img\{random_img}")
          label_bg = Label(self.root, image = self.bg)
          label_bg.place(x=0,y=0, relwidth=1, relheight=1)

          # Frame
          frame = Frame(self.root, bg = "white")
          frame.place(x=270 ,y=90, width=800, height=550)


          # heading label
          register_label = Label(frame, text="Register", font=("times new roman",30,'bold'), fg="black", bg="white")
          register_label.place(x=325, y=10)




          # F_name label
          first_name_label=Label(frame, text="First name", font=("times new roman",15,'bold'), fg="black", bg="white")
          first_name_label.place(x=150, y=75)

          # f_name entry_box
          self.first_name_entry = ttk.Entry(frame, textvariable=self.var_f_name, font=("times new roman",15,'bold'))
          self.first_name_entry.place(x=150, y=105, width=200)


          #l_name label
          last_name_label=Label(frame, text="Last name", font=("times new roman",15,'bold'), fg="black", bg="white")
          last_name_label.place(x=450, y=75)

          #l_name entry_box
          self.last_name_entry = ttk.Entry(frame, textvariable=self.var_l_name, font=("times new roman",15,'bold'))
          self.last_name_entry.place(x=450, y=105, width=200)



          #Contact label
          contact_label=Label(frame, text="Contact number", font=("times new roman",15,'bold'), fg="black", bg="white")
          contact_label.place(x=150, y=145)

          #contact entry_box
          self.contact_entry = ttk.Entry(frame, font=("times new roman",15,'bold'))
          self.contact_entry.place(x=150, y=175, width=200)


          #Email label
          eamil_label=Label(frame, text="E-mail", font=("times new roman",15,'bold'), fg="black", bg="white")
          eamil_label.place(x=450, y=145)

          #Email entry_box
          self.eamil_entry = ttk.Entry(frame, font=("times new roman",15,'bold'))
          self.eamil_entry.place(x=450, y=175, width=200)


          #Security Question label
          security_label=Label(frame, text="Select Security Quetions", font=("times new roman",15,'bold'), fg="black", bg="white")
          security_label.place(x=150, y=215)

          # Security Question Combobox
          self.security_combobox = ttk.Combobox(frame, font=("times new roman",15,'bold'), state="readonly")
          self.security_combobox['value'] = ("Select", "Your Birth Place?", "Your Pet Name?", "Your Teacher name?", "Your School name?") 
          self.security_combobox.place(x=150, y=245, width=200)
          self.security_combobox.current(0)

          #Security Answer label
          security_answer_label=Label(frame, text="Security Answer", font=("times new roman",15,'bold'), fg="black", bg="white")
          security_answer_label.place(x=450, y=215)

          #Security Answer entry_box
          self.security_answer_entry = ttk.Entry(frame, font=("times new roman",15,'bold'))
          self.security_answer_entry.place(x=450, y=245, width=200)


          #Password label
          passwd_label=Label(frame, text="Password", font=("times new roman",15,'bold'), fg="black", bg="white")
          passwd_label.place(x=150, y=285)

          #Password entry_box
          self.passwd_entry = ttk.Entry(frame, font=("times new roman",15,'bold'))
          self.passwd_entry.place(x=150, y=315, width=200)


          #Confirm Password label
          confirm_passwd_label=Label(frame, text="Confirm Password", font=("times new roman",15,'bold'), fg="black", bg="white")
          confirm_passwd_label.place(x=450, y=285)

          #Confirm Paswword entry_box
          self.confirm_passwd_entry = ttk.Entry(frame, font=("times new roman",15,'bold'))
          self.confirm_passwd_entry.place(x=450, y=315, width=200)



          # Register btn
          register_btn = Button(frame, text="Register",  font=("times new roman",15,'bold'), bd=3, relief=RIDGE, fg='white', bg='black', activebackground="black", activeforeground="white", cursor="hand2") 
          register_btn.place(x= 200 , y= 375, width=120, height=35)

          # login now btn
          login_btn = Button(frame, text="Back to Login?",  font=("times new roman",10,'bold'), borderwidth=0, fg='black', bg='white', activebackground="white", activeforeground="black", cursor="hand2")
          login_btn.place(x= 500 , y= 375, width=150)



if __name__ == "__main__":
     root = Tk()
     app = Register_win(root)

     root.mainloop()

