from tkinter import* 
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import random


class Login_win:
     def __init__(self, root):
          self.root = root
          self.root.title("Login")
          self.root.geometry("1550x800+0+0")
          # self.root.attributes("-fullscreen", True)

          all_img = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
          random_img = random.choice(all_img)
          self.bg = ImageTk.PhotoImage(file = rf"G:\Peoples Projects\Anuraag TY Peoject\Resturante Mangement system\bg-img\{random_img}")
          label_bg = Label(self.root, image = self.bg)
          label_bg.place(x=0,y=0, relwidth=1, relheight=1)


          # frame
          frame = Frame(self.root, bg = "black")
          frame.place(x=510 ,y=170, width=340, height=450)


          # user image
          user_img = Image.open(r"G:\Peoples Projects\Anuraag TY Peoject\Resturante Mangement system\user1.png")
          user_img = user_img.resize((100,100), Image.ANTIALIAS)

          self.photo_img = ImageTk.PhotoImage(user_img)
          label_img = Label(image = self.photo_img, bg ="black", borderwidth=0)
          label_img.place(x=630, y=175, width = 100, height = 100)


          # label
          get_start = Label(frame, text="Get Started", font=("times new roman",20,'bold'), fg="white", bg="black")
          get_start.place(x=96, y=100)


          # label
          username=Label(frame, text="Username", font=("times new roman",15,'bold'), fg="white", bg="black")
          username.place(x=75, y=145)

          # entry_box
          self.txtuser = ttk.Entry(frame, font=("times new roman",15,'bold'))
          self.txtuser.place(x=75, y=175, width=200)

          # label
          password=Label(frame, text="Password", font=("times new roman",15,'bold'), fg="white", bg="black")
          password.place(x=75, y=210)

          # entry_box
          self.txtpass = ttk.Entry(frame, font=("times new roman",15,'bold'), show="*")
          self.txtpass.place(x=75, y=245, width=200)


          # Login btn
          login_btn = Button(frame, text="Login",  font=("times new roman",15,'bold'), bd=3, relief=RIDGE, fg='white', bg='red', activebackground="red", activeforeground="white", command=self.user_login, cursor="hand2")
          login_btn.place(x= 115 , y= 300, width=120, height=35)

          # register btn
          register_btn = Button(frame, text="New user register",  font=("times new roman",10,'bold'), borderwidth=0, fg='white', bg='black', activebackground="black", activeforeground="white", cursor="hand2")
          register_btn.place(x= 15 , y= 350, width=150)


          # forget btn
          forget_btn = Button(frame, text="forget password",  font=("times new roman",10,'bold'), borderwidth=0, fg='white', bg='black', activebackground="black", activeforeground="white", cursor="hand2")
          forget_btn.place(x= 10 , y= 375, width=150)

     def user_login(self):
          if self.txtuser.get() == "" or  self.txtpass.get() == "":
               messagebox.showerror("Error", "All Field Required")
          elif self.txtuser.get() == "ank" or  self.txtpass.get() == "123":
               messagebox.showinfo("Success", "Welcome sir!")
          else:
               messagebox.showerror("Warning", "invalid Username And Password")
                    





if __name__ == "__main__":
     root = Tk()
     app = Login_win(root)
     root.mainloop()

