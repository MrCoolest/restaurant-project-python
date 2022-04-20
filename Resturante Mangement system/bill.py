
try:
     from tkinter import *
     import random
     import os
     from tkinter import messagebox
except Exception as e:
     print(f"something is worng with importing files: {e}")     

class Bill_App:
     def __init__(self,root):
          self.root = root
          width = root.winfo_screenwidth()
          height = root.winfo_screenheight()
          # print(width)
          # print(height)
          self.root.geometry("%dx%d" %(1366, 768))
          # self.root.geometry("%dx%d" %(1300, 700))
          self.root.title("Billing Application")
          # bg_color = "#074463"
          bg_color = "orange"
          title = Label(self.root, text='Billing Application',bd=12, relief=GROOVE, bg=bg_color, fg="white", font=('times new roman', 30, 'bold'),pady=2).pack(fill=X)
          # =================== Variables =============================
          # =================== Cosmetics =============================
          self.soap = IntVar()
          self.face_cream = IntVar()
          self.face_wash = IntVar()
          self.spray = IntVar()
          self.gell = IntVar()
          self.loshan = IntVar()

          # =================== Grocery =================================
          self.rice = IntVar()
          self.food_oil = IntVar()
          self.daal = IntVar()
          self.wheat = IntVar()
          self.sugar = IntVar()
          self.tea = IntVar()

          # =================== Cold Drinks==============================
          self.maza = IntVar()
          self.cock = IntVar()
          self.frooti = IntVar()
          self.thunmsup = IntVar()
          self.limca = IntVar()
          self.sprite = IntVar()

          # ============Total Products Price & Tax Varibales=============
          self.cosmetic_price = StringVar()
          self.grocery_price = StringVar()
          self.cold_drink_price = StringVar()


          self.cosmetic_tax = StringVar()
          self.grocery_tax = StringVar()
          self.cold_drink_tax = StringVar()

          # ==========================Customer===========================

          self.c_name = StringVar()
          self.c_phone = StringVar()
          self.bill_no = StringVar()
          x = random.randint(1000,9999)
          self.bill_no.set(x) 
          self.search_bill = StringVar()

          ################## Customer Detail frame ####################
          f1 = LabelFrame(self.root, bd=10, relief=GROOVE,text="Customer Details",font=("times new roman" ,15,'bold'), fg='white',bg=bg_color)
          f1.place(x=0, y=80, relwidth=1)

          cname_lbl = Label(f1, text="Customer Name", bg=bg_color, fg='white', font=("times new roman",17,"bold")).grid(row=0, column=0, padx= 20, pady=10)
          cname_txt = Entry(f1, width=17, textvariable=self.c_name, font=('arial', 15 ), bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

          
          cphone_lbl = Label(f1, text="Phone No:", bg=bg_color, fg='white', font=("times new roman",17,"bold")).grid(row=0, column=2, padx= 20, pady=10)
          cphone_txt = Entry(f1, width=15, textvariable=self.c_phone,font=('arial', 15 ), bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)


          c_bill_lbl = Label(f1, text="Bill No:", bg=bg_color, fg='white', font=("times new roman",17,"bold")).grid(row=0, column=4, padx= 20, pady=10)
          c_bill_txt = Entry(f1, width=15, textvariable=self.search_bill,font=('arial', 15 ), bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)  

          bill_btn = Button(f1, text="Search", command=self.find_bill , width=10, bd=7, font=("arial",12,'bold')).grid(row=0, column=6, pady=10, padx=20)



          # ################# cosmetics frame #####################
          f2 = LabelFrame(self.root, bd=10, relief=GROOVE,text="Cosmetics",font=("times new roman" ,15,'bold'), fg='white',bg=bg_color)
          f2.place(x=5, y=180, width=325 , height=380)

          bath_lbl = Label(f2, text="Bath Soap", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=0, column=0, padx = 10, pady=10, sticky="w")
          bath_txt = Entry(f2, width=10,textvariable=self.soap, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=0, column=1, padx =10, pady=10)

          face_cream_lbl = Label(f2, text="Face Cream", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=1, column=0, padx = 10, pady=10, sticky="w")
          face_cream_txt = Entry(f2, width=10,textvariable=self.face_cream, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=1, column=1, padx =10, pady=10)

          face_w_lbl = Label(f2, text="Face Wash", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=2, column=0, padx = 10, pady=10, sticky="w")
          face_w_txt = Entry(f2, width=10,textvariable=self.face_wash, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=2, column=1, padx =10, pady=10)

          hair_s_lbl = Label(f2, text="Hair Spray", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=3, column=0, padx = 10, pady=10, sticky="w")
          hair_s_txt = Entry(f2, width=10, textvariable=self.spray,font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=3, column=1, padx =10, pady=10)

          hair_g_lbl = Label(f2, text="Hair Gel", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=4, column=0, padx = 10, pady=10, sticky="w")
          hair_g_txt = Entry(f2, width=10, textvariable=self.gell, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=4, column=1, padx =10, pady=10)

          body_l_lbl = Label(f2, text="Body Lotion", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=5, column=0, padx = 10, pady=10, sticky="w")
          body_l_txt = Entry(f2, width=10, textvariable=self.loshan, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=5, column=1, padx =10, pady=10)


          # ################# Cold Drink frame #####################
          f3 = LabelFrame(self.root, bd=10, relief=GROOVE,text="Cold Drink",font=("times new roman" ,15,'bold'), fg='white',bg=bg_color)
          f3.place(x=330, y=180, width=325 , height=380)

          c1_lbl = Label(f3, text="Maza", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=0, column=0, padx = 10, pady=10, sticky="w")
          c1_txt = Entry(f3, width=10,textvariable=self.maza, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=0, column=1, padx =10, pady=10)

          c2_lbl = Label(f3, text="Coca Cola", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=1, column=0, padx = 10, pady=10, sticky="w")
          c2_txt = Entry(f3, width=10, textvariable=self.cock, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=1, column=1, padx =10, pady=10)

          c3_lbl = Label(f3, text="Frooti", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=2, column=0, padx = 10, pady=10, sticky="w")
          c3_txt = Entry(f3, width=10,textvariable=self.frooti, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=2, column=1, padx =10, pady=10)

          c4_lbl = Label(f3, text="Thumbs up", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=3, column=0, padx = 10, pady=10, sticky="w")
          c4_txt = Entry(f3, width=10, textvariable=self.thunmsup, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=3, column=1, padx =10, pady=10)

          c5_lbl = Label(f3, text="Limca", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=4, column=0, padx = 10, pady=10, sticky="w")
          c5_txt = Entry(f3, width=10,textvariable=self.limca, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=4, column=1, padx =10, pady=10)

          c6_lbl = Label(f3, text="Sprite", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=5, column=0, padx = 10, pady=10, sticky="w")
          c6_txt = Entry(f3, width=10,textvariable=self.sprite, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=5, column=1, padx =10, pady=10)


           # ################# Grocery frame #####################
          f4 = LabelFrame(self.root, bd=10, relief=GROOVE,text="Grocery",font=("times new roman" ,15,'bold'), fg='white',bg=bg_color)
          f4.place(x=655, y=180, width=325 , height=380)

          g1_lbl = Label(f4, text="Rice", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=0, column=0, padx = 10, pady=10, sticky="w")
          g1_txt = Entry(f4, width=10,textvariable=self.rice, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=0, column=1, padx =10, pady=10)

          g2_lbl = Label(f4, text="Food oil", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=1, column=0, padx = 10, pady=10, sticky="w")
          g2_txt = Entry(f4, width=10,textvariable=self.food_oil, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=1, column=1, padx =10, pady=10)

          g3_lbl = Label(f4, text="Daal", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=2, column=0, padx = 10, pady=10, sticky="w")
          g3_txt = Entry(f4, width=10,textvariable=self.daal, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=2, column=1, padx =10, pady=10)

          g4_lbl = Label(f4, text="Wheat", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=3, column=0, padx = 10, pady=10, sticky="w")
          g4_txt = Entry(f4, width=10,textvariable=self.wheat, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=3, column=1, padx =10, pady=10)

          g5_lbl = Label(f4, text="Sugar", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=4, column=0, padx = 10, pady=10, sticky="w")
          g5_txt = Entry(f4, width=10,textvariable=self.sugar, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=4, column=1, padx =10, pady=10)

          g6_lbl = Label(f4, text="Tea", font=("times new roman",16,'bold'), bg=bg_color, fg="white").grid(row=5, column=0, padx = 10, pady=10, sticky="w")
          g6_txt = Entry(f4, width=10,textvariable=self.tea, font=("times new roman",16,'bold'),bd=5, relief=SUNKEN).grid(row=5, column=1, padx =10, pady=10)

          #  ================== Bill Area ========================
          f5 = Frame(self.root,bd=10, relief=GROOVE)
          f5.place(x=1000,y=180, width=350, height=380)

          bill_title = Label(f5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

          scroll_y = Scrollbar(f5, orient=VERTICAL)
          self.textarea = Text(f5, yscrollcommand=scroll_y.set)
          scroll_y.pack(side=RIGHT, fill=Y)
          scroll_y.config(command=self.textarea.yview)
          self.textarea.pack(fill=BOTH, expand=1)

          # ======= Button Frame =======
          f6 = LabelFrame(self.root, bd=10, relief=GROOVE,text="Bill Menu",font=("times new roman" ,15,'bold'), fg='white',bg=bg_color)
          f6.place(x=0, y=560, relwidth=1 , height=140)
          
          m1_lbl = Label(f6, bg = bg_color, fg= 'white',text="Total Cosmetic Price", font=("times new romans", 14, "bold")).grid(row=0, column=0, padx = 20, pady=1, sticky='w')
          m1_txt = Entry(f6, width=18,textvariable=self.cosmetic_price, font="arial 10 bold", bd = 7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

          m2_lbl = Label(f6, bg = bg_color, fg= 'white',text="Total Grocery Price", font=("times new romans", 14, "bold")).grid(row=1, column=0, padx = 20, pady=1, sticky='w')
          m2_txt = Entry(f6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd = 7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)


          m3_lbl = Label(f6, bg = bg_color, fg= 'white',text="Total Cold Drink Price", font=("times new romans", 14, "bold")).grid(row=2, column=0, padx = 20, pady=1, sticky='w')
          m3_txt = Entry(f6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd = 7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
          


          c1_lbl = Label(f6, bg = bg_color, fg= 'white',text="Cosmetic Tax", font=("times new romans", 14, "bold")).grid(row=0, column=2, padx = 20, pady=1, sticky='w')
          c1_txt = Entry(f6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd = 7, relief=SUNKEN).grid(row=0, column=4, padx=10, pady=1)

          c2_lbl = Label(f6, bg = bg_color, fg='white',text="Grocery Tax", font=("times new romans", 14, "bold")).grid(row=1, column=2, padx = 20, pady=1, sticky='w')
          c2_txt = Entry(f6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd = 7, relief=SUNKEN).grid(row=1, column=4, padx=10, pady=1)


          c3_lbl = Label(f6, bg = bg_color, fg='white',text="Cold Drinks  Tax", font=("times new romans", 14, "bold")).grid(row=2, column=2, padx = 20, pady=1, sticky='w')
          c3_txt = Entry(f6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd = 7, relief=SUNKEN).grid(row=2, column=4, padx=10, pady=1)


          btn_f = Frame(f6,relief=GROOVE, bd=7,)
          btn_f.place(x=780, width=560, height=105)

          total_btn = Button(btn_f, text="Total", command=self.total,bg='black', fg="white", pady=15, width=11,bd=5, font="arial 12 bold").grid(row=0, column= 0, padx= 5, pady=5)
          G_Bill_btn = Button(btn_f, text="Genrate Bill", command=self.bill_area, bg='black', fg="white", pady=15, width=11,bd=5, font="arial 12 bold").grid(row=0, column= 1, padx= 5, pady=5)
          Clear_btn = Button(btn_f, text="Clear",command=self.clear_data  , bg='black', fg="white", pady=15, width=11,bd=5, font="arial 12 bold").grid(row=0, column= 2, padx= 5, pady=5)
          Exit_btn = Button(btn_f, text="Exit", command=self.Exit_app, bg='black', fg="white", pady=15, width=11,bd=5, font="arial 12 bold").grid(row=0, column= 3, padx= 5, pady=5)
          self.welcome_bill()

     def total(self):

          self.c_s_p = self.soap.get()*40
          self.c_fc_p = self.face_cream.get()*120 
          self.c_fw_p = self.face_wash.get()*60 
          self.c_sp_p = self.spray.get()*180
          self.c_g_p = self.gell.get()*140
          self.c_l_p = self.loshan.get()*180

          self.total_cosmetic_price = float(
                                   self.c_s_p+  
                                   self.c_fc_p+  
                                   self.c_fw_p+  
                                   self.c_sp_p+
                                   self.c_g_p+  
                                   self.c_l_p
                                   )
                                   
          self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
          self.c_tax = round((self.total_cosmetic_price*0.05),2)
          self.cosmetic_tax.set("Rs. "+str(self.c_tax))     

          self.g_r_p = self.rice.get()*80 
          self.g_fo_p = self.food_oil.get()*180
          self.g_d_p = self.daal.get()*60
          self.g_w_p = self.wheat.get()*240
          self.g_s_p = self.sugar.get()*45
          self.g_t_p = self.tea.get()*150

          self.total_grocery_price = float(
               self.g_r_p+  
               self.g_fo_p+  
               self.g_d_p+  
               self.g_w_p+  
               self.g_s_p+  
               self.g_t_p
               )
          self.grocery_price.set("Rs. "+str(self.total_grocery_price))
          self.g_tax = round((self.total_grocery_price*0.1),2)
          self.grocery_tax.set("Rs. "+str(self.g_tax))     
           
          self.cd_m_p =  self.maza.get()*60
          self.cd_c_p =  self.cock.get()*60
          self.cd_f_p =  self.frooti.get()*50
          self.cd_th_p = self.thunmsup.get()*50
          self.cd_l_p = self.limca.get()*40
          self.cd_s_p = self.sprite.get()*60

          self.total_coldDrink_price = float(
               self.cd_m_p+  
               self.cd_c_p+  
               self.cd_f_p+  
               self.cd_th_p+  
               self.cd_l_p+  
               self.cd_s_p
               )

          self.cold_drink_price.set("Rs. "+str(self.total_coldDrink_price))
          self.cd_tax = round((self.total_coldDrink_price*0.05),2)
          self.cold_drink_tax.set("Rs. "+str(self.cd_tax))     

          self.Total_bill = float(
                                   self.total_cosmetic_price+
                                   self.total_grocery_price+
                                   self.total_coldDrink_price+ 
                                   self.c_tax+
                                   self.g_tax+
                                   self.cd_tax
                                   )
     def welcome_bill(self):
          self.textarea.delete('1.0', END)
          self.textarea.insert(END,"\t Welcome Retail")
          self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
          self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
          self.textarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
          self.textarea.insert(END,f"\n======================================")
          self.textarea.insert(END,f"\nProduct\t\tQTY\t\tPrice")
          self.textarea.insert(END,f"\n======================================")

     def bill_area(self):
          if self.c_name.get() == "" or self.c_phone.get() == "":
               messagebox.showerror("Error", "Customer Detail is Must!")
          elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == 'Rs. 0.0':   
               messagebox.showinfo("Empty", "No Products Selected")  
          else :     
               self.welcome_bill()
               if self.soap.get()!=0:
                    self.textarea.insert(END,f"\n Bath Soap \t\t{self.soap.get()}\t\t{self.c_s_p}")
               if self.face_cream.get()!=0:
                    self.textarea.insert(END,f"\n Face Cream \t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
               if self.face_wash.get()!=0:
                    self.textarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
               if self.spray.get()!=0:
                    self.textarea.insert(END,f"\n Spray \t\t{self.spray.get()}\t\t{self.c_sp_p}")
               if self.gell.get()!=0:
                    self.textarea.insert(END,f"\n Gel \t\t{self.gell.get()}\t\t{self.c_g_p}")
               if self.loshan.get()!=0:
                    self.textarea.insert(END,f"\n Lotion \t\t{self.loshan.get()}\t\t{self.c_l_p}")


               if self.rice.get()!=0:
                    self.textarea.insert(END,f"\n Rice \t\t{self.rice.get()}\t\t{self.g_r_p}")
               if self.food_oil.get()!=0:
                    self.textarea.insert(END,f"\n Food oil \t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
               if self.daal.get()!=0:
                    self.textarea.insert(END,f"\n Daal \t\t{self.daal.get()}\t\t{self.g_d_p}")
               if self.wheat.get()!=0:
                    self.textarea.insert(END,f"\n Wheat \t\t{self.wheat.get()}\t\t{self.g_w_p}")
               if self.sugar.get()!=0:
                    self.textarea.insert(END,f"\n Sugar \t\t{self.sugar.get()}\t\t{self.g_s_p}")
               if self.tea.get()!=0:
                    self.textarea.insert(END,f"\n Tea \t\t{self.tea.get()}\t\t{self.g_t_p}")


               if self.maza.get()!=0:
                    self.textarea.insert(END,f"\n Maza \t\t{self.maza.get()}\t\t{self.cd_m_p}")
               if self.cock.get()!=0:
                    self.textarea.insert(END,f"\n Coca Cola \t\t{self.cock.get()}\t\t{self.cd_c_p}")
               if self.frooti.get()!=0:
                    self.textarea.insert(END,f"\n Frooti \t\t{self.frooti.get()}\t\t{self.cd_f_p}")
               if self.thunmsup.get()!=0:
                    self.textarea.insert(END,f"\n Thumsup \t\t{self.thunmsup.get()}\t\t{self.cd_th_p}")
               if self.limca.get()!=0:
                    self.textarea.insert(END,f"\n Limca \t\t{self.limca.get()}\t\t{self.cd_l_p}")
               if self.sprite.get()!=0:
                    self.textarea.insert(END,f"\n Sprite \t\t{self.sprite.get()}\t\t{self.cd_s_p}")

               self.textarea.insert(END,f"\n--------------------------------------")
               if self.cosmetic_tax.get() != "Rs. 0.0":
                    self.textarea.insert(END,f"\nCosmetics Tax\t\t\t{self.cosmetic_tax.get()}")
               if self.grocery_tax.get() != "Rs. 0.0":
                    self.textarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
               if self.cold_drink_tax.get() != "Rs. 0.0":
                    self.textarea.insert(END,f"\nColdrink Tax\t\t\t{self.cold_drink_tax.get()}")
               self.textarea.insert(END,f"\n======================================")    
               self.textarea.insert(END,f"\nTotal bill : \t\t\t Rs. {self.Total_bill}")
               self.save_bill()

     def save_bill(self):
          op = messagebox.askyesno('Save Bill', "Do you want to save the Bill ?")
          if op>0:
               self.bill_data = self.textarea.get('1.0',END)
               f1 = open("customers_bill\\"+str(self.bill_no.get())+'.txt',"w")
               f1.write(self.bill_data)
               f1.close()
               messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Succefully!")
          else:
               return     

     def find_bill(self):
          present = "no" 
          for i in os.listdir("customers_bill\\"):
               if i.split('.')[0] == self.search_bill.get():
                    f1 = open("customers_bill\\"+i,"r")
                    self.textarea.delete('1.0',END)
                    for d in f1:
                         self.textarea.insert(END, d)
                    f1.close()
                    present = "yes"
          if present == 'no':
               messagebox.showerror("Error","Invalid Bill number")          


     def clear_data(self):
          op = messagebox.askyesno("Clear", "Do You really want to clear")
          if op > 0:
               # =================== Cosmetics =============================
               self.soap.set(0)
               self.face_cream.set(0)
               self.face_wash.set(0)
               self.spray.set(0)
               self.gell.set(0)
               self.loshan.set(0)

               # =================== Grocery =================================
               self.rice.set(0)
               self.food_oil.set(0)
               self.daal.set(0)
               self.wheat.set(0)
               self.sugar.set(0)
               self.tea.set(0)

               # =================== Cold Drinks==============================
               self.maza.set(0)
               self.cock.set(0)
               self.frooti.set(0)
               self.thunmsup.set(0)
               self.limca.set(0)
               self.sprite.set(0)

               # ============Total Products Price & Tax Varibales=============
               self.cosmetic_price.set("")
               self.grocery_price.set("")
               self.cold_drink_price.set("")


               self.cosmetic_tax.set("")
               self.grocery_tax.set("")
               self.cold_drink_tax.set("")

               # ==========================Customer===========================

               self.c_name.set("")
               self.c_phone.set("")
               self.bill_no.set("")
               x = random.randint(1000,9999)
               self.bill_no.set(x) 
               self.search_bill.set("")

               self.welcome_bill()
     
     def Exit_app(self):
          op = messagebox.askyesno("Exit", "Do You really want to exit")
          if op > 0:
               self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()