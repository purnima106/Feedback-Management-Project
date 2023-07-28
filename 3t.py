from tkinter import *
from tkinter.messagebox import * 
from tkinter import messagebox 
from tkinter.scrolledtext import *
from sqlite3 import *


root = Tk()
root.title("Feedback Form")
root.geometry("800x620+420+50")
root.resizable(0 ,0)
root.configure(bg = "peru")
root.iconbitmap("fb.ico")
f = ("Cambria" , 30 , "bold")

lab_hl = Label(root , text = " Welcome to COFFEE WORLD CAFE🥤🍵🥤" , font =f)
lab_hl.pack(pady = 5) 

# main panel

def customer() : 
	mw.deiconify()
	root.withdraw()

def manager() : 
	sw.deiconify()
	root.withdraw()

btn1_user = Button(root , text =  "Customer Panel", font = ("Arial Black" , 18 , "bold") , fg = "black" , bg = "yellow" , width = 16 , height = 2 , relief = 'solid' , bd = 2 , command = customer  )
btn1_user.place(x = 60, y = 220) 


btn1_admin = Button(root , text =  "Manager Panel", font = ("Arial Black" , 18 , "bold") , fg = "black" , bg = "yellow" , width = 16 , height = 2 , relief = 'solid' , bd = 2 , command = manager  )
btn1_admin.place(x = 460, y = 220) 



mw = Toplevel(root)
mw.title("User Feedback Form")
mw.iconbitmap("fb.ico")
mw.geometry("1525x800+0+2")
mw.configure(bg = "peru")
mw.resizable(0,0)
sf = ("Cambria" , 20 , "bold")


lab_hd = Label(mw , text = "We Welcome your Feedback" , font = f)
lab_hd.place(x = 900 , y = 0)

lab_feedback = Label(mw , text = "Feedback here -> " ,  font =f)
lab_feedback.place(x = 900 , y = 130)


lab_name = Label(mw , text = "Enter Name: " , font = f)
lab_name.place(x = 680 , y = 230)

ent_name = Entry(mw , font = sf , bd = 2)
ent_name.place(x = 1000 , y = 230)

lab_email = Label(mw , text = "Enter email id : " , font = sf)
lab_email.place(x = 640 , y = 300)

ent_email = Entry(mw , font =sf)
ent_email.place(x = 1050 , y = 300)

lab_fb = Label(mw , text = "Enter feedback here -> " , font =sf) 
lab_fb.place(x = 640 , y = 400)

scr_fb = ScrolledText(mw ,  font = sf , width = 20 , height = 4 )
scr_fb.place(x = 1050 , y = 400)

lab_rate = Label(mw , text = "Rate us :" , font = sf ) 
lab_rate.place(x = 640 , y = 600) 

r = IntVar()
f = ("Bookman Old Style" , 22 , "bold")

rb_rating1 = Radiobutton(mw , variable = r , value = 1 , font = f , bg = "white")
rb_rating2 = Radiobutton(mw , variable = r , value = 2 , font = f , bg = "white")
rb_rating3 = Radiobutton(mw , variable = r , value = 3 , font = f , bg = "white")


nf = ("Bookman Old Style" , 18 , "bold")
lab_rating1 = Label(mw , text = "Need to improve" , font = f)
lab_rating2 = Label(mw , text = "Average" , font = f )
lab_rating3 = Label(mw , text = "Excellent" , font = f )



rb_rating1.place(x = 1090 , y = 600)
rb_rating2.place(x = 1290 , y = 600)
rb_rating3.place(x = 1450 , y = 600)


lab_rating1.place(x = 1000 , y = 640)
lab_rating2.place(x = 1260 , y = 640)
lab_rating3.place(x = 1400 , y = 640)

def submit() :
	try :
		con = None
		con = connect("cw.db")
		cursor = con.cursor()
		name = ent_name.get()
		if (name == "") or (name.strip() =="") :
			showerror("Wrong" , "Name should not be empty")
			ent_name.delete(0 , END)
			ent_name.focus()
			return
		if (not name.isalpha()) :
			showerror("Wrong" , "Invalid name")
			ent_name.delete(0 , END)
			ent_name.focus()
			return

		email = ent_email.get()
		if (email == "") or (email.strip() == "") : 
			showerror("Wrong" , "Email should not be empty")
			ent_email.focus()
			return
		if  "@gmail.com" not in email :
			showerror("Wrong" , "invalid email format")
			ent_email.delete(0 , END)
			ent_email.focus()
			return

		if (len(email) >= 20) : 
			showerror("Wrong" , "Invalid email format")
			ent_email.delete(0 , END)
			ent_email.focus()
			return
	
		feedback = scr_fb.get(1.0 , END) 
		if (feedback.strip() == "") :
			showerror("Wrong" , "Feedback should not be empty")
			return
		
		rating = ""
		if r.get() == 3 : 
			rating = "Excellent"
		elif r.get() == 2 : 
			rating = "Average"
		else :		
			rating = "Need to improve"
		sql = "insert into record values('%s','%s' ,'%s' ,'%s')"
		cursor.execute(sql%(name,email,feedback,rating))
		con.commit()
		showinfo("Submitted", "Thank You for ur Response" )
		ent_name.delete(0 , END)
		ent_email.delete(0 , END)
		scr_fb.delete(1.0, END)
		r.set(3)
		return
	except Exception as e : 
		showerror("Wrong" , e)
		ent_name.delete(0 , END)
		ent_email.delete(0 , END)
		scr_fb.delete(1.0, END)
		r.set(3)
		return
	finally : 
		if con is not None :
			con.close()

btn_submit = Button(mw, text = "Submit" , font = ("Bookman Old Style" , 20 , "bold") , width = 10 , command = submit )
btn_submit.place(x = 1200 , y = 700)

def back() : 
	root.deiconify()
	mw.withdraw()

btn_back = Button(mw, text = "Back" , font = ("Bookman Old Style" , 20 , "bold") , width = 5 ,command = back)
btn_back.place(x = 1420 , y = 700)

mw.withdraw()


sw = Toplevel(root)
sw.title("Manager Login")
sw.iconbitmap("fb.ico")
sw.geometry("750x500+420+50")
sw.configure(bg = "dark grey")
sw.resizable(0 ,0)


lab_hl2 = Label(sw , text = "Manager Login" , font = ("Sitka Text Semibold" , 31 , 'bold') , bg = "#FFEBCD" , fg = "black" , relief = "solid")
lab_hl2.pack(pady = 1) 
sw.withdraw()	

lab_username = Label(sw , text = "Enter Username : " , font = ("Bookman Old Style" , 17 , "bold") ,  bg = "#EEE8CD" , fg = "#006400" )
lab_username.place(x = 270 , y = 145)

ent_username = Entry(sw ,  font = ("Bookman Old Style" , 15 , "bold"))
ent_username.place(x = 268 , y = 190)

lab_password = Label(sw , text = "Enter Password : " , font = ("Bookman Old Style" , 17 , "bold") ,  bg = "#EEE8CD" , fg = "#006400" )
lab_password.place(x = 270 , y = 240)

ent_password = Entry(sw ,  font = ("Bookman Old Style" , 15 , "bold") , show = "*")
ent_password.place(x = 268 , y = 285)
  
def login() : 
	username = ent_username.get()
	password = ent_password.get()
	if (username != "CoffeeWorld") and (password != "cw@123" ):  
		showerror("Wrong" , "Invalid username and password")
		ent_username.delete(0 , END)
		ent_password.delete(0 , END)
		ent_username.focus()
		return
	if (username != "CoffeeWorld") : 
		showerror("Wrong" , "Invalid username")
		ent_username.delete(0 , END)
		ent_username.focus()
		return
	if (password != "cw@123" ):  
		showerror("Wrong" , "Invalid password")
		ent_password.delete(0 , END)
		ent_password.focus()
		return

	showinfo("Welcome" , "Login successfull")
	tw.deiconify()
	sw.withdraw()
	ent_username.delete(0 , END)
	ent_password.delete(0 , END)
	ent_username.focus()
	return
	
	
btn_mlogin = Button(sw , text = "Login" , font = ("Bookman Old Style" , 18 , "bold") ,  bg = "#FCE6C9" , fg = "#CD1076" , relief = "solid", command = login ) 
btn_mlogin.place(x = 340 , y = 330)

def mhome() : 
	root.deiconify()
	sw.withdraw()
btn_mback = Button(sw , text = "Home" , font = ("Bookman Old Style" , 18 , "bold") ,  bg = "#FCE6C9" , fg = "#CD1076" , relief = "solid" , command = mhome ) 
btn_mback.place(x = 340 , y = 400)

tw = Toplevel(root)
tw.title("Admin Login")
tw.geometry("750x500+420+50")
tw.resizable(0,0)
tw.configure(bg = "dark grey")
tw.iconbitmap("fb.ico")

def view():
    nw.deiconify()
    tw.withdraw()

    con = None
    try:
        con = connect("cw.db")
        cursor = con.cursor()
        sql = "select * from record"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info += "Name: " + str(d[0]) + "\n"
            info += "Email: " + str(d[1]) + "\n"
            info += "Feedback: " + str(d[2]) + "\n"
            info += "Rating: " + str(d[3]) + "\n"
            info += "\n"

        scr_view.delete(1.0, END)  # Clear the existing content
        scr_view.insert(INSERT, info)
    except Exception as e:
        con.rollback()
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()


btn_view = Button(tw , text = "View feedback " , width = 12 , font = ("Lucida Calligraphy" , 22 , "bold") , bg = "#E5E5E5" , fg = "#8B3A62" , relief = "solid", command = view)
btn_view.place(x = 240 , y = 55)

def hhome() : 
	root.deiconify()
	tw.withdraw()

btn_hhome = Button(tw , text = "Go to Home" , width = 12 , font = ("Lucida Calligraphy" , 22 , "bold") , bg = "#E5E5E5" , fg = "#8B3A62" , relief = "solid", command = hhome)
btn_hhome.place(x = 240 , y = 400) 


def delete() : 
	lw.deiconify()
	tw.withdraw()
	
btn_delete = Button(tw , text = "Delete feedback " , width = 12,  font = ("Lucida Calligraphy" , 22 , "bold") , bg = "#E5E5E5" , fg = "#8B3A62" , relief = "solid" , command = delete)
btn_delete.place(x = 240 , y = 145 )

tw.withdraw()


nw = Toplevel(root)
nw.title("View Feeback")
nw.geometry("1440x600+5+50")
nw.resizable(0 ,0)
nw.configure(bg = "brown")
nw.iconbitmap("fb.ico")
nw.configure(bg = "peru")
scr_view = ScrolledText(nw , font = ("Bookman Old Style" , 25 , "bold") , width = 62 , height = 10)
scr_view.place(x =40 , y = 50)

def bview() : 
	tw.deiconify()
	nw.withdraw()

btn_bview = Button(nw , text = "Back" , font = ("Bookman Old Style" , 25 , "bold") , width = 10 , command = bview , fg = "#4B0082" , bg = "#FFFAF0" )
btn_bview.place(x = 50 , y = 510)


nw.withdraw()

lw = Toplevel(root)
lw.title("Delete Feeback")
lw.geometry("750x500+420+50")
lw.resizable(0 ,0)
lw.configure(bg = "light grey")
lw.iconbitmap("fb.ico")
lw.configure(bg = "peru")

lw_lab_name = Label(lw , text = "Enter name : " , font = ("Bookman Old Style" , 25 , "bold") , fg = "#808000" , bg = "#FDF5E6")
lw_lab_name.place(x = 300 , y = 40 )

lw_ent_name = Entry(lw , font = ("Bookman Old Style" , 22 , "bold"))
lw_ent_name.place(x = 220 , y = 120 )

def delete_() :
    
	con = None
	try : 
		con = connect("cw.db")
		cursor = con.cursor()
		sql = "delete from records  where name = '%s' "
		name = lw_ent_name.get()
		if (name == "") or (name.strip() == "") : 
			showerror("Wrong" , "Name should not be empty")
			lw_ent_name.delete(0 , END)
			lw_ent_name.focus()
			return
		cursor.execute(sql%(name))
		if cursor.rowcount == 1 : 
			if askyesno("Quit", "Do you want to delete?"):
				lw.protocol("WM_DELETE_WINDOW", on_closing)
				con.commit()
				showinfo("Success" , "Feedback deleted")
				lw_ent_name.delete(0 , END)
				lw_ent_name.focus()
				return
		else : 
			showerror("Failed" , "Name does not exists")
			lw_ent_name.delete(0 , END)
			lw_ent_name.focus()
			return

	except Exception as e : 
		showerror("Wrong" , e)
		lw_ent_name.delete(0 , END)
		lw_ent_name.focus()
		return
	finally : 
		if con is not None : 
			con.close()

btn_delete = Button(lw , text = "Delete" , font = ("Bookman Old Style" , 25 , "bold") , fg = "black" , bg = "#808000" , width = 10 , command = delete_)
btn_delete.place(x = 300 , y = 220) 

def hback() : 
	tw.deiconify()
	lw.withdraw()

btn_hback = Button(lw , text = "Back" , font = ("Bookman Old Style" , 25 , "bold") , fg = "black" , bg = "#808000" , width = 10 , command = hback)
btn_hback.place(x = 300 , y = 320) 

lw.withdraw()

def on_closing():
    if askyesno("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)
sw.protocol("WM_DELETE_WINDOW", on_closing)
tw.protocol("WM_DELETE_WINDOW", on_closing)
nw.protocol("WM_DELETE_WINDOW", on_closing) 
lw.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
