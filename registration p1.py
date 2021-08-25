from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image,ImageTk #pip install pillow
import pymysql #pip install pymysql

class Register:

    def __init__(self,root):
       self.root = root
       self.root.title("Registration Window")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="white")

       self.bg = ImageTk.PhotoImage(file="image/photo4.jpg")
       bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

       self.left = ImageTk.PhotoImage(file="image/prio.jpg")
       left = Label(self.root,image=self.left).place(x=80, y=100, width=400, height=500)

       frame1  = Frame(self.root,bg="white")
       frame1.place(x=480,y=100,width=700,height=500)
       title = Label(frame1,text='REGISTER HERE',font=("times new roman",20,'bold'),bg="white",fg="green").place(x=50,y=30)



       f_name = Label(frame1,text="First Name",font=("times new roman",15,'bold'),bg="white",fg='gray').place(x=0,y=100,width=230)

       self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_fname.place(x=50,y=130,width=230)

       l_name = Label(frame1, text="Last Name", font=("times new roman", 15,'bold'), bg="white", fg='gray').place(
          x=370, y=100)

       self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.txt_lname.place(x=370, y=130, width=230)


       contact_name = Label(frame1, text="Contact Name", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=170)

       self.txt_contact_entry = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.txt_contact_entry.place(x=50, y=200, width=230)

       self.Email_entry = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.Email_entry.place(x=370, y=200, width=230)

       Email_name = Label(frame1, text="Email", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=370, y=170)


       self.gender = ttk.Combobox(frame1, font=("times new roman", 12),state="readonly",justify=CENTER)

       self.gender ['values']=("Select","Female","Male","Others")

       self.gender .place(x=50, y=260, width=230)
       self.gender .current(0)
       gender = Label(frame1, text="Gender", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=230)


       self.answer_entry = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.answer_entry.place(x=370, y=260, width=230)

       answer_name = Label(frame1, text="Answer", font=("times new roman", 15, 'bold'), bg="white",
                             fg='gray').place(
          x=370, y=230)

       pass_word = Label(frame1, text="Password", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=295)

       self.pass_word_entry = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.pass_word_entry.place(x=50, y=330, width=230)


       cpass_word = Label(frame1, text="Confirm password", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=370, y=295)
       # button part in programing

       self.cpass_word = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.cpass_word.place(x=370, y=330, width=230)

       self.var_chk=IntVar()
       chk=Checkbutton(frame1,text="Agree",variable=self.var_chk,onvalue=1 ,offvalue=0,font=("times new roman", 15)).place(x=50,y=380)

       self.btn_image=ImageTk.PhotoImage(file="image/regis.png")
       bn=Button(frame1,image=self.btn_image,bd=0,cursor="hand2",command= self.register_data).place(x=250,y=400,width=150, height=50)

       bn = Button(self.root,text="Sign In",font=("times new roman", 15),bd=1, cursor="hand2",width=10).place(x=230, y=520)

    def clear(self):
        self.txt_fname.delete(0,END)
        self. txt_lname.delete(0,END)
        self.txt_contact_entry.delete(0,END)
        self.Email_entry.delete(0,END)
        self.answer_entry.delete(0,END)
        self.pass_word_entry.delete(0,END)
        self.cpass_word.delete(0,END)
        self.gender.current(0)




    def register_data(self):
      if self.txt_fname.get()=="" or self.txt_contact_entry.get()=="" or  self.Email_entry.get()=="" or   self.gender.get()=="Select" or self.answer_entry.get() =="" or  self.pass_word_entry.get() =="" or self.cpass_word.get() =="":
         messagebox.showerror("Error","All Fields Are Required", parent=self.root)

      elif self.pass_word_entry.get() != self.cpass_word.get():
         messagebox.showerror("Error", "Password not same", parent=self.root)

      elif self.var_chk.get()==0:
         messagebox.showerror("Error", "Please Agree Our all Condition and press registration button again", parent=self.root)

      else:


       try:
          con=pymysql.connect(host="localhost",user="root", password="",database="employ2")
          cur=con.cursor()
          cur.execute("select * from emp where email =%s",self.Email_entry.get())
          row=cur.fetchone()

          if row!=None:
              messagebox.showerror("Error", "User already Exist ",
                                   parent=self.root)

          else:

              cur.execute("insert into emp(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                          (self.txt_fname.get()
                           ,self.txt_lname.get(),
                           self.txt_contact_entry.get(),
                           self.Email_entry.get(),
                           self.gender.get(),
                           self.answer_entry.get(),
                           self.pass_word_entry.get()

                           ))
              con.commit()
              messagebox.showinfo("Done","Register Successful",parent=self.root)
              self.clear()

       except Exception as es:
          messagebox.showerror("Error", f"Error due to:{str(es)}",
                               parent=self.root)
                




root=Tk()
object=Register(root)
root.mainloop()
